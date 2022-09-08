#                           Universidade Tecnológica Federal do Paraná                              # 
#                                        Computação Gráfica                                         #
#                                      Eduarda Simonis Gavião                                       #
#                                          Fernanda Azevedo                                         #
#________________________________________________###________________________________________________#
# |Para iniciar a coleta de coordenadas abra o menu, clicando com o scroll do mouse                |#
# |Utilizando o mouse:                                                                             |#
# |                  Para setar os pontos basta clicar na área dimensionada                        |#
# |                  Com menos de 3 pontos não é possivel criar uma figura                         |#
# |Utilizando o teclado:                                                                           |#                       
# |                  Para setar os pontos, digite as coordenadas de x e y                          |# 
# |Teclas especiais:                                                                               |#
# |                   V ou v-> Criar pelo teclado                                                  |#        
# |                   T ou t -> Transformação Geométrica                                           |#
# |                   M ou m -> Criar pelo mouse                                                   |#
# |                   D ou d -> Deletear uma forma                                                 |#
# |                   A ou a -> Criar por aresta                                                   |#
# |                   Esc -> A tela é deletada e o sistema fechado                                 |#
# |Exemplo de transformadas geométricas:                                                           |#
# |  Translação: 0,10,10                                                                           |#
# |  Escala: 0.5,1.5,0.5                                                                           |#
# |  Rotação: 30,1,0,0                                                                             |#
# |  Reflexão: X, Y, X & Y                                                                         |#
# |  Cisalhamento: SH = 0.3                                                                        |#
# |________________________________________________________________________________________________|#

#Chamada das bibliotecas
from itertools import count
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import numpy as np 

formas = []
TGs = []

def init():
    
    glClearColor(0.0, 0.0, 0.0, 1.0)

    gluOrtho2D(-100.0, 100.0,-100.0,100.0)  
  
# Função para desenhar eixos cartesianos  
def desenhaEixos():
    
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
    glBegin(GL_LINES)
    glColor3f(255, 255, 255)
    glVertex2i(100, 0)
    glVertex2i(-100, 0)
    glVertex2i(0, 100)
    glVertex2i(0, -100)
    for point in range(-11, 11):
        glVertex2i(point*10, -1)
        glVertex2i(point*10, 1)
        glVertex2i(-1, point*10)
        glVertex2i(1, point*10)
    glEnd()

def MenuPrincipal():
    pass

# Função para menu teclado
def MenuTeclado(options,x,y):
    
    global win
    if options == b'v':
        if options==b'3':
          criar_por_teclado(3)   
    if options == b'VT':
        criar_por_teclado() 
    if options == b'm':
        criar_por_mouse()  
    if options == b'M':
        criar_por_mouse()  
    if options == b'a':
        criar_por_aresta()
    if options == b'A':
        criar_por_aresta()
    if options == b't':
        criar_TG()
    if options == b'T':
        criar_TG()  
    if options == b'd':
        deletar()      
    if options == b'D':
        deletar()    
       
    if options == b'\x1b':
        glutDestroyWindow(win)
        sys.exit()
    glutPostRedisplay()

# Criar formas geométricas atraves do vertice    
def criar_por_teclado(forma_geometrica):
    
    forma = []
    
    for i in range(0, forma_geometrica):
        x, y = input("Entra com x,y: ").replace(" ", "").split(',')
        tuple = [int(x), int(y)]
        
        forma.append(tuple)
        
    if verifica_forma(forma):
        formas.append(forma)
    else:
        print('Parâmetros inválidos')

    return 0

# Função para capturar clicks do mouse
def Mouse(button, state, x, y):
    
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            x_click = (x-400)/2 +100
            y_click =-(y-400)/2 -100

            adiciona_ponto(x_click,y_click)
            print(x_click)
            print(y_click)

# Função para criar a forma geometrica por mouse
def criar_por_mouse(forma_geometrica):
    
    print(forma_geometrica)
    global ler_mouse
    ler_mouse = True
    global forma_click
    forma_click = []
    global num_vertice
    num_vertice = forma_geometrica

    return 0

def reseta_mouse():
    
    global ler_mouse
    ler_mouse = False
    global forma_click
    forma_click = []
    global num_vertice
    num_vertice = 1

    return 0

# Função para criar a forma geometrica por aresta
def criar_por_aresta(forma_geometrica):
    
    forma = []

    x, y = input("Digite o x,y do centro: ").replace(" ", "").split(',')
    x = int(x)
    y = int(y)

    aresta = int(input("Defina o tamanho da aresta: "))
    
    # Calcula vértices do triangulo
    if forma_geometrica == 3:
        r = (aresta/math.sqrt(3))/2
        print(r)
        x_a = x - (aresta/2)
        y_a = y - r
        tuple = [int(x_a), int(y_a)]
        forma.append(tuple)
        
        x_a = x
        y_a = y + 2*r
        tuple = [int(x_a), int(y_a)]
        forma.append(tuple)

        x_a = x + (aresta/2)
        y_a = y - r 
        tuple = [int(x_a), int(y_a)]
        forma.append(tuple)

        formas.append(forma)
    
    # Calcula vértices do quadrado
    elif forma_geometrica == 4:
        x_a = x - (aresta/2)
        y_a = y - (aresta/2)
        tuple = [int(x_a), int(y_a)]
        forma.append(tuple)
        
        x_a = x - (aresta/2)
        y_a = y + (aresta/2)
        tuple = [int(x_a), int(y_a)]
        forma.append(tuple)

        x_a = x + (aresta/2)
        y_a = y + (aresta/2)
        tuple = [int(x_a), int(y_a)]
        forma.append(tuple)

        x_a = x + (aresta/2)
        y_a = y - (aresta/2)
        tuple= [int(x_a), int(y_a)]
        forma.append(tuple)

        formas.append(forma)

    # Calcula vértices do hexágono
    elif forma_geometrica == 6:
        x_a = x - (aresta/2)
        y_a = y + aresta
        tuple= [int(x_a), int(y_a)]
        forma.append(tuple)
        
        x_a = x + (aresta/2)
        y_a = y + aresta
        tuple= [int(x_a), int(y_a)]
        forma.append(tuple)

        x_a = x + aresta
        y_a = y
        tuple= [int(x_a), int(y_a)]
        forma.append(tuple)

        x_a = x + (aresta/2)
        y_a = y - aresta
        tuple = [int(x_a), int(y_a)]
        forma.append(tuple)

        x_a = x - (aresta/2)
        y_a = y - aresta
        tuple = [int(x_a), int(y_a)]
        forma.append(tuple)

        x_a = x - aresta
        y_a = y
        tuple= [int(x_a), int(y_a)]
        forma.append(tuple)

        formas.append(forma)

    return 0

# Transformadas geométricas
def criar_TG(TG_selected):
    
    if TG_selected == 1 or TG_selected== 2:
        x, y, z = input("Digite os valores para x,y,z: ").replace(" ", "").split(',')
        tuple = (float(x), float(y), float(z))
        TGs.append([TG_selected, tuple])        

    elif TG_selected  == 3:
        w, x, y, z = input("Digite os valores para w,x,y,z: ").replace(" ", "").split(',')
        tuple = (float(w), float(x), float(y), float(z))
        TGs.append([TG_selected, tuple])       
    
    elif TG_selected == 4:
        print("Escolha o eixo de reflexão")
        eixo = input(" 1 - x | 2 - y | 3 - x e y : ")
        if eixo == '1':
            tuple = (1, -1, 1)
            TGs.append([2, tuple])
        elif eixo == '2':
            tuple = (-1, 1, 1)
            TGs.append([2, tuple])
        elif eixo == '3':
            tuple = (-1, -1, 1)
            TGs.append([2, tuple])
        else:
            print("Valor inválido")

    elif TG_selected  == 5:
        shx = float(input("SH: "))
        TGs.append([TG_selected, shx])       

    return 0

# Função para verificar nova forma
def verifica_forma(lista):
    
    # Verifica se todos os elementos são únicos    
    verificados = []
    valor_repetido = any(valor in verificados or verificados.append(valor) for valor in lista)
    if(valor_repetido):
        return 0

    # Verifica se todos os elementos estão dentro da tela
    for vertice in lista:
        vertice_valido = all(num >= -100 and num <=100 for num in vertice)
        if not vertice_valido:
            return 0
    return 1

ler_mouse = False
forma_click = []
num_vertice = 1

# Função para adicionar ponto
def adiciona_ponto(x, y):
    
    print('clicks: ',forma_click, ' ler mouse: ', ler_mouse, ' num_vertice: ', num_vertice)

    if ler_mouse and len(forma_click)  < num_vertice:
        tuple= [int(x), int(y)]        
        forma_click.append(tuple)
        print(forma_click)
        
    elif ler_mouse and len(forma_click) == num_vertice:
        if verifica_forma(forma_click):
            formas.append(forma_click)
        else:
            print('Parâmetros inválidos')
        reseta_mouse()
    else:
        return 0

# Função para deletar o poligono
def deletar(indice):
    
    del formas[indice]
    
    return 0

# Função para imprimir figuras 
def imprimeFigura():    
   
    i=1    
    
    for forma in formas:      
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix() 
        
        # Aplica a transformada geometrica        
        for TG in TGs:
            TG_selected = TG[0]
            TG_valores = TG[1]
            print(TG, ' ', TG_selected)
            
            if TG_selected == 1:
                glTranslatef(TG_valores[0], TG_valores[1], TG_valores[2])           
                
            elif TG_selected  == 2:
                glScalef(TG_valores[0], TG_valores[1], TG_valores[2])
                
            elif TG_selected== 3:
                sum_x = np.sum(forma, axis=0)[0]
                sum_y = np.sum(forma, axis=0)[1]
                count = len(forma)

                centro_x = sum_x/count
                centro_y = sum_y/count
                glTranslatef(centro_x, centro_y, 0)
                glRotatef(TG_valores[0], TG_valores[1], TG_valores[2], TG_valores[3])
                glTranslatef(-centro_x, -centro_y, 0)

            elif TG_selected == 5:
                sum_x = np.sum(forma, axis=0)[0]
                sum_y = np.sum(forma, axis=0)[1]
                count = len(forma)

                centro_x = sum_x/count
                centro_y = sum_y/count

                glTranslatef(centro_x, centro_y, 0)
                
                # Matriz de cisalhamento
                sh = [  1.0, 0.0, 0.0, 0.0,
                        TG_valores, 1.0, 0.0, 0.0,
                        0.0, 0.0, 1.0, 0.0,
                        0.0, 0.0, 0.0, 1.0]
                glMultMatrixf(sh)
                glTranslatef(-centro_x, -centro_y, 0)               
                     
        # Plota Figuras       
        
        glBegin(GL_POLYGON)   
        for vertice in forma:
            x = vertice[0]
            y = vertice[1]
            cores(i)
            glVertex2f(x, y)                
        i+=1
        glEnd()       
        glPopMatrix()           
        
    return 0

# Função para alterar as cores para cada poligono
def cores(i):
    
    if (i==1): # Poligono 1
        cor=glColor3f(0, 1, 0) #define a cor dos pontos
    if(i==2): # Poligono 2
        cor=glColor3f(0, 0, 1) #define a cor dos pontos
    if(i==3): # Poligono 3
        cor=glColor3f(1, 0, 0) #define a cor dos pontos
    if(i==4): # Poligono 4
        cor=glColor3f(1, 0, 1) #define a cor dos pontos
    if(i==5): # Poligono 5
        cor=glColor3f(1, 1, 0) #define a cor dos pontos
        
#criação das opções do menu     
def Menu():
    
    # Submenu para criar os pontos por teclado com vertice
    sub_menu_vertice = glutCreateMenu(criar_por_teclado)
    glutAddMenuEntry("Triangulo", 3)
    glutAddMenuEntry("Quadrado", 4)
    glutAddMenuEntry("Hexagono", 6)
    
    # Submenu para criar os pontos por mouse
    sub_menu_mouse = glutCreateMenu(criar_por_mouse)
    glutAddMenuEntry("Triangulo", 3)
    glutAddMenuEntry("Quadrado", 4)
    glutAddMenuEntry("Hexagono", 6)

    # Submenu para criar os pontos por aresta
    sub_menu_central = glutCreateMenu(criar_por_aresta)
    glutAddMenuEntry("Triangulo", 3)
    glutAddMenuEntry("Quadrado", 4)
    glutAddMenuEntry("Hexagono", 6)

    # Submenu com as transformações geométricas
    sub_menu_TG = glutCreateMenu(criar_TG)
    glutAddMenuEntry("Translacao", 1)
    glutAddMenuEntry("Escala", 2)
    glutAddMenuEntry("Rotacao", 3)
    glutAddMenuEntry("Reflexao", 4)
    glutAddMenuEntry("Cisalhamento", 5)

    # Submenu para deletar as formas geometricas
    sub_menu_deletar = glutCreateMenu(deletar)    
    
    quantidade_formas = 0
    
    # Verifica a quantidade de formas geometricas    
    for forma in formas:
        texto = "Figura " + str(quantidade_formas+1) + ": " + str(forma)
        glutAddMenuEntry(texto, quantidade_formas)
        quantidade_formas+= 1

    menu = glutCreateMenu(MenuPrincipal)  
    glutAddSubMenu("Utilizar o teclado", sub_menu_vertice)   
    glutAddSubMenu("Utilizar o mouse", sub_menu_mouse)
    glutAddSubMenu("Utilizar ponto central", sub_menu_central)
    glutAddSubMenu("Transformacao geometrica", sub_menu_TG)
    glutAddSubMenu("Apagar forma geometrica", sub_menu_deletar)    
    
    glutAttachMenu(GLUT_MIDDLE_BUTTON)

    return 0  

def Janela():
    
    # Limpe os buffers de cor e profundidade
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Plot dos eixos
    desenhaEixos()    
    
    # Plot das figuras
    imprimeFigura()    
    
    Menu()
    
    # Força execução dos comendos GLs em tempo finito
    glFlush()

#função main para a chamada das funções necessárias 
if __name__ == "__main__":
    
    global i
    glutInit()

    glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH | GLUT_RGB)
    
    glutInitWindowSize(400, 400)
    glutCreateWindow("PyOpenGL - TG")
    
    glutDisplayFunc(Janela)
    glutMouseFunc(Mouse)    
    glutKeyboardFunc(MenuTeclado)    

    init()

    glutMainLoop()
