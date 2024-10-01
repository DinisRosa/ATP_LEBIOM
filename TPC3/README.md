# RESUMO DO TPC3
## DATA: 23/09/2024
## AUTOR: DSBR

## RESUMO:
O TPC3 consistiu em emplementar o jogo dos 21 fósforos em python:
* O jogador começa -> PlayerStart(): O PC irá ganhas sempre
* O pc começa -> PcStart(): O PC perde se o jogador não fizer erros de calculo; se o mesmo fizer, o PC passa para a frente e ganha.

Erro Atual: em PcStart()
* quando o jogador faz um erro de calculo, o PC não consegue manter a liderança e acaba por quase perder, isto é: jogador joga e sobra 1 mas o pc vai jogar e fazer os fosforos ficarem negativos e dizer que ganha.


