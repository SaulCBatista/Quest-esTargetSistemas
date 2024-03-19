'''
4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.
Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

Resposta: Se a restrição for que eu só posso ir duas vezes a uma mesma sala, não há como definir qual interrupto acende a lâmpada de cada sala.
Mas se for possivel ir duas vezes mas em salas diferentes, processo seria:

1 - Ligo interrupto 1, verifico sala 1;
2 - Desligo interrupto 1, Ligo interrupto 2, verifico sala 2;

Se a lâmpada da sala 1 ligou, o interrupto 1 é da sala 1.
Se a lâmpada não ligou, o interrupto 1 é da sala 2 ou 3.

Se a lâmpada da sala 2 ligou, o inturrupto é da sala 2
Se a lâmpada não ligou, o interrupto é da sala 1 ou 3.

Caso a lâmpada da sala 1 ligou e a lâmpada da sala 2 ligou, interrupto 1 = lâmpada 1, interrupto 2 = lâmpada 2, interrupto 3 = lâmpada 3.
Caso a lâmpada da sala 1 NÃO ligou e a lâmpada da sala 2 ligou, interrupto 1 = lâmpada 3, interrupto 2 = lâmpada 2, inturrpto 3 = sala 1.
Caso a lâmpada da sala 1 ligou e a lâmpada da sala NÃO 2 ligou, interrupto 1 = lâmpada 1, interrupto 2 = lâmpada 3, interrupto 3 = lâmpada 2.
Caso a lâmpada da sala 1 NÃO ligou e a lâmpada da sala 2 NÃO ligou, interrupto 1 = lâmpada 2, interrupto 2 = lâmpada 1, interrupto 3 = lâmpada 3.
'''