# Mudanças

## 1.2.0 (22/10/2026)

- Nova opção «Usar o meu CSS» (desligada de fábrica), e o botão «Editar o meu CSS» ao lado dela: o `meu.css` é uma folha SUA, livre (cor e layout), que o Hefesto põe por cima do tema e aplica ao salvar, sem reabrir a janela. Fica em `~/.local/state/hefesto-dualsense4unix/mods/tema-claro/meu.css`, nasce com um exemplo comentado e sobrevive às atualizações da extensão.
- Não vale `url()`, `@import`, funções de imagem, `expression()`, barra invertida nem «<»; passando de 16 KB, ou errando uma chave, o arquivo inteiro fica sem valer e a janela da extensão diz a linha.
- Pede o Hefesto que conhece a opção do tipo `css` (a mesma API 2): um Hefesto anterior recusa o manifesto, então quem não atualizou o Hefesto fica na 1.1.0.

## 1.1.0 (22/10/2026)

- A extensão também escolhe o lado dos botões da janela: fechar, maximizar e minimizar vão para a esquerda (`"botoes": "esquerda"` no bloco `tema`).
- Duas opções, «Cores claras» e «Botões à esquerda», ambas ligadas de fábrica: cor e lado se escolhem separados e valem na hora, com a janela aberta.
- Pede o Hefesto que lê o lado dos botões no bloco `tema` (a mesma API 2): um Hefesto anterior recusa o bloco com mais de uma chave e não liga o tema, então quem não atualizou o Hefesto fica na 1.0.0.

## 1.0.0 (20/10/2026)

- A extensão nasce: o fundo claro, os textos escuros, os sete destaques e as cores das categorias da aba Conexões, medidos pela régua de contraste do Hefesto.
- A logo ganha o disco escuro de sempre (`--logo-fundo`) e o aro claro (`--logo-aro`): as cores dela não mudam.
- O fundo em volta da janela fica claro (`--fundo-da-pagina`), um tom abaixo do fundo da interface.
- Ligar e desligar valem na hora, com a janela aberta (Hefesto com o tema ao vivo).
