# hefesto-mod-tema-claro

A interface do Hefesto em fundo claro, com os textos e os destaques escuros que passam na régua de contraste.

> **Aviso.** Extensão independente: troca só as cores da interface do Hefesto. Não roda programa nenhum e não lê nada da sua casa.

## O que ela faz

O [Hefesto](https://github.com/Hefesto-Team/hefesto-dualsense4unix) nasce escuro. Esta extensão é só um
manifesto e uma folha de cores (`tema.css`): o bloco `:root{…}` com os tokens da casa trocados por um fundo
claro, textos quase pretos e os sete destaques (verde, ciano, roxo, laranja, rosa, vermelho, amarelo)
escurecidos até ficarem legíveis sobre o branco. As cores das categorias da aba Conexões também escurecem.

O Hefesto mede a folha antes de ligar: cada texto passa de 4,5:1 e cada destaque de 3:1 sobre os três fundos.
As cores dos plásticos dos controles não mudam: a luz do controle é a mesma em qualquer tema.
A logo também fica a de sempre: o tema põe atrás dela o disco escuro, com um aro claro, e o fundo em volta da janela fica claro também.

O tema troca na hora: a chave da aba Experimental liga ou desliga, e a janela aberta repinta sem fechar, com a barra de cima e as listas do sistema no claro.

## Instalar

```bash
hefesto-dualsense4unix mod instalar https://github.com/Hefesto-Team/hefesto-mod-tema-claro
hefesto-dualsense4unix mod ligar tema-claro
```

O Hefesto mostra o aviso acima antes de instalar e pede o «sim». A extensão instalada pelo git se atualiza
sozinha. Também se instala de uma pasta local (`mod instalar /caminho/da/pasta`), e essa nunca se atualiza
sozinha.

Voltar ao escuro: `hefesto-dualsense4unix mod desligar tema-claro`. Remover:
`hefesto-dualsense4unix mod remover tema-claro`.

## Testes

```bash
python3 -m pytest testes
```

Só a biblioteca padrão do Python e o `pytest`: os testes refazem a conta de contraste da régua do Hefesto
sobre a folha. Com o Hefesto importável no mesmo Python, passam a folha também pela régua dele.

## Licença

MIT, de Vitória Maria e André Farias.
