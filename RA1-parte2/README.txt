Realizamos os testes com números, letras, palavras
Teste n1  Conjunto1=(alecrim, z , 69, adrey, 10)
	  Conjunto2=(y, queijo, 24, pano)
Realizamos 4 operações, a primeira foi união, e o resultado foi:
União: conjunto 1 ['alecrim', 'z', '69', 'andrey', '10'], conjunto 2 ['y', 'queijo', '24', 'pano']. Resultado: {'24', 'alecrim', 'z', '69', 'y', 'queijo', 'andrey', 'pano', '10'}

A segunda operação realizada foi intersecção, e o resultado foi:
Interseção: conjunto 1 ['alecrim', 'z', '69', 'andrey', '10'], conjunto 2 ['y', 'queijo', '24', 'pano']. Resultado: set(). obs: o conjunto ficou vazio pois não há intersecção.

A terceira operação realizada foi Diferença e o resultado foi:
Diferença: conjunto 1 ['alecrim', 'z', '69', 'andrey', '10'], conjunto 2 ['y', 'queijo', '24', 'pano']. Resultado: {'alecrim', 'z', '69', 'andrey', '10'}

A quarta operação realizada foi Produto Cartesiano e o resultado foi:
Produto cartesiano: conjunto 1 ['alecrim', 'z', '69', 'andrey', '10'], conjunto 2 ['y', 'queijo', '24', 'pano']. Resultado:
('alecrim', 'y')
('alecrim', 'queijo')
('alecrim', '24')
('alecrim', 'pano')
('z', 'y')
('z', 'queijo')
('z', '24')
('z', 'pano')
('69', 'y')
('69', 'queijo')
('69', '24')
('69', 'pano')
('andrey', 'y')
('andrey', 'queijo')
('andrey', '24')
('andrey', 'pano')
('10', 'y')
('10', 'queijo')
('10', '24')
('10', 'pano')

Agora, para finalizar, um exemplo utilizando intersecção e diferença para provar que de fato programamos corretamente :)
C1= 1,2,3,4,5
C2= 5,4,3,6

Resultado:
Interseção: conjunto 1 ['1', '2', '3', '4', '5'], conjunto 2 ['5', '4', '3', '6']. Resultado: {'3', '5', '4'}
Diferença: conjunto 1 ['1', '2', '3', '4', '5'], conjunto 2 ['5', '4', '3', '6']. Resultado: {'2', '1'}
