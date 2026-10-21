"""A folha do tema claro, medida pela mesma conta da régua do Hefesto (``mods/tema.py``)."""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parents[1]
MANIFESTO = json.loads((RAIZ / "hefesto-mod.json").read_text(encoding="utf-8"))
FOLHA = (RAIZ / MANIFESTO["tema"]["arquivo"]).read_text(encoding="utf-8")

TEXTOS = ("--fg", "--texto-suave", "--texto-mudo", "--comment", "--rot-campo")
FUNDOS = ("--app-bg", "--panel", "--elevated")
ACENTOS = ("--green", "--cyan", "--purple", "--orange", "--pink", "--red", "--yellow")
PROIBIDO = re.compile(r"url\(|@import|\\|var\(|!important", re.IGNORECASE)


def _tokens(folha: str) -> dict[str, str]:
    corpo = re.fullmatch(r"\s*:root\s*\{([^{}]*)\}\s*", folha)
    assert corpo, "a folha é um bloco :root{…} só"
    pares = (d.split(":", 1) for d in corpo.group(1).split(";") if d.strip())
    return {k.strip(): v.strip() for k, v in pares}


def _luminancia(cor: str) -> float:
    canais = [int(cor[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in canais]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def _contraste(a: str, b: str) -> float:
    claro, escuro = sorted((_luminancia(a), _luminancia(b)), reverse=True)
    return (claro + 0.05) / (escuro + 0.05)


TOKENS = _tokens(FOLHA)


def test_o_manifesto_e_so_tema_sem_processo() -> None:
    assert MANIFESTO["tipos"] == ["tema"]
    assert MANIFESTO["permissoes"] == ["tema"]
    assert "processo" not in MANIFESTO
    assert len(FOLHA.encode("utf-8")) <= 16 * 1024


def test_a_folha_nao_carrega_nada_de_fora() -> None:
    assert not PROIBIDO.search(FOLHA)
    assert not any(k.startswith(("--cosmic", "--starlight", "--galactic", "--white"))
                   for k in TOKENS), "as cores dos plásticos são do controle, não do tema"


@pytest.mark.parametrize(("grupo", "piso"), [(TEXTOS, 4.5), (ACENTOS, 3.0)])
def test_cada_texto_e_cada_destaque_passa_sobre_cada_fundo(grupo: tuple[str, ...],
                                                           piso: float) -> None:
    for cor in grupo:
        for fundo in FUNDOS:
            assert re.fullmatch(r"#[0-9a-f]{6}", TOKENS[cor]), cor
            assert _contraste(TOKENS[cor], TOKENS[fundo]) >= piso, (cor, fundo)


def test_o_rotulo_de_campo_segue_o_verde() -> None:
    assert TOKENS["--rot-campo"] == TOKENS["--green"]


def test_a_regua_do_hefesto_aceita_a_folha() -> None:
    tema = pytest.importorskip("hefesto_dualsense4unix.mods.tema")
    aceito = tema.validar(FOLHA)
    assert aceito.tokens["--app-bg"] == TOKENS["--app-bg"]


def test_a_logo_ganha_o_disco_escuro_de_sempre() -> None:
    """A logo do Hefesto fica a de sempre: o tema religa o disco escuro atrás dela, com o aro claro."""
    assert TOKENS["--logo-fundo"] == "radial-gradient(circle at 35% 30%,#3b2d5c,#1a1b24 70%)"
    assert TOKENS["--logo-aro"] == TOKENS["--linha"]


def test_o_fundo_em_volta_da_janela_fica_um_tom_abaixo_do_fundo() -> None:
    """A moldura clara: abaixo do ``--app-bg``, como o ``#11121a`` da casa fica abaixo do ``#21222c``."""
    assert TOKENS["--fundo-da-pagina"] == "#dde1ea"
    assert _luminancia(TOKENS["--fundo-da-pagina"]) < _luminancia(TOKENS["--app-bg"])
    assert _contraste(TOKENS["--fg"], TOKENS["--fundo-da-pagina"]) >= 4.5
