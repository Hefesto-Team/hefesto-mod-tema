# hefesto-mod-tema-claro

A interface do Hefesto em fundo claro, com os textos e os destaques escuros que passam na régua de contraste.

> **Aviso.** Extensão independente: troca as cores da interface do Hefesto e o lado dos botões de fechar, maximizar e minimizar. Não roda programa nenhum e não lê nada da sua casa.

## O que ela faz

O [Hefesto](https://github.com/Hefesto-Team/hefesto-dualsense4unix) nasce escuro. Esta extensão é só um
manifesto e uma folha de cores (`tema.css`): o bloco `:root{…}` com os tokens da casa trocados por um fundo
claro, textos quase pretos e os sete destaques (verde, ciano, roxo, laranja, rosa, vermelho, amarelo)
escurecidos até ficarem legíveis sobre o branco. As cores das categorias da aba Conexões também escurecem.

O Hefesto mede a folha antes de ligar: cada texto passa de 4,5:1 e cada destaque de 3:1 sobre os três fundos.
As cores dos plásticos dos controles não mudam: a luz do controle é a mesma em qualquer tema.
A logo também fica a de sempre: o tema põe atrás dela o disco escuro, com um aro claro, e o fundo em volta da janela fica claro também.

O tema troca na hora: a chave da aba Experimental liga ou desliga, e a janela aberta repinta sem fechar, com a barra de cima e as listas do sistema no claro.

## Os botões da janela (1.1.0)

O Hefesto põe os botões de fechar, maximizar e minimizar do lado que o sistema usa (no COSMIC, à direita). Esta
extensão os leva para a **esquerda**, na ordem fechar, maximizar, minimizar. Cor e lado são duas opções separadas,
no botão de configurações da extensão, e as duas vêm ligadas:

| opção | liga | desliga |
| --- | --- | --- |
| Cores claras | o fundo claro | volta ao escuro |
| Botões à esquerda | os botões vão para a esquerda | voltam ao lado do sistema |

Dá para ter só o lado (cores desligadas) ou só a cor (botões desligados). Desligar a extensão inteira devolve as
duas coisas. Tudo vale na hora, com a janela aberta. O lado vai no bloco `tema` do manifesto
(`"botoes": "esquerda"`), e cada escolha liga a sua opção por `cor_pela_opcao` e `botoes_pela_opcao`: o Hefesto
recusa um lado que não seja `esquerda` ou `direita` e um vínculo com opção que não existe ou não é do tipo `ligado`.

## O meu CSS (1.2.0)

A folha do tema só troca cores, e passa pela régua de contraste. Para mexer no resto (bordas, tamanhos, espaços),
a opção **Usar o meu CSS**, desligada de fábrica, liga uma folha SUA por cima do tema. No botão de configurações da
extensão, **Editar o meu CSS** cria o arquivo `meu.css` com um exemplo comentado (na pasta de dados da extensão,
`~/.local/share/hefesto-dualsense4unix/mods/tema-claro/`) e o abre no seu editor. Salvou, a janela aberta repinta
na hora. O arquivo é seu: a atualização da extensão não o toca.

Vale cor e layout. Não vale `url()`, `@import`, funções de imagem, `expression()`, barra invertida nem «<», e o
teto é 16 KB. Se o arquivo não vale, ele inteiro fica de fora e a janela da extensão diz a linha que errou.

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
