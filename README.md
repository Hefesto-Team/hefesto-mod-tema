# hefesto-mod-tema

O **Gerenciador de Tema** do Hefesto: Escuro ou Claro, um tema seu, a cor de destaque, o lado dos botões da janela,
a sua logo e o seu CSS. O Hefesto o traz de fábrica, ligado no Escuro.

> Não roda programa nenhum e não lê nada da sua casa: é um manifesto e uma folha de cores.

## O que ele faz

O [Hefesto](https://github.com/Hefesto-Team/hefesto-dualsense4unix) nasce escuro. Na janela da extensão, aba
Experimental, as opções se arrumam em quatro abas:

| aba | opção | o que faz |
| --- | --- | --- |
| Cores | Tema | Escuro (o da casa), Claro (`tema.css`) ou Importado |
| Cores | Arquivo | aparece com Importado: um `.css` só com o bloco `:root{…}` |
| Destaque | Cor | com a bolinha da aba acesa, a cor das chaves e dos realces |
| Janela | Botões | Do sistema, Esquerda ou Direita: o lado de fechar, maximizar e minimizar |
| Janela | Logo | uma imagem sua no lugar da logo |
| CSS | Meu CSS | uma folha sua por cima da interface |

Tudo vale na hora, com a janela aberta. Desligar a extensão devolve o Escuro, a logo e os botões do sistema.

## O que o Hefesto confere

O que você importa é dado, nunca código, e passa pela régua antes de valer:

- **Tema importado e Claro:** cada texto passa de 4,5:1 e cada destaque de 3:1 sobre os três fundos. Não vale
  `url()`, `@import`, `var()`, barra invertida nem `!important`.
- **Cor de destaque:** a que não passa de 3:1 sobre os fundos do tema não liga, e a janela diz por quê na linha.
- **Logo:** PNG, JPEG ou WebP, conferida pelos bytes, até 256 KB e de 16 a 1024 px de lado. SVG nunca.
- **Meu CSS:** cor e layout; não vale `url()`, `@import`, funções de imagem, `expression()`, barra invertida nem
  «<», e o teto é 16 KB. Ele vale dentro da interface: os botões da janela moram na barra de cima, fora do
  alcance dele, e nenhum tema os esconde.

A cópia do que você importa mora na pasta de dados da extensão, e a atualização não a toca.

## Instalar

O install do Hefesto já a traz e liga. À mão:

```bash
hefesto-dualsense4unix mod instalar https://github.com/Hefesto-Team/hefesto-mod-tema
hefesto-dualsense4unix mod ligar gerenciador-de-tema
```

A extensão instalada pelo git se atualiza sozinha. Ela substitui a antiga `tema-claro`: instalar a nova tira a
antiga e traz as escolhas dela (Claro e botões à esquerda) e o `meu.css`.

## Testes

```bash
python3 -m pytest testes
```

Só a biblioteca padrão do Python e o `pytest`. Com o Hefesto importável no mesmo Python, o manifesto e a folha
passam também pela régua dele.

## Licença

MIT, de Vitória Maria e André Farias.
