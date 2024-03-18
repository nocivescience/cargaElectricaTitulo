from manim import *
class MyCharge(Scene):
    def construct(self):
        mySentence1=Text("Primeras estimaciones")
        mySentence2=MarkupText("De lo que se convertiría en nuetros días")
        mySentence3=Text('en el pilar de la civilización como la conocemos...')
        for myText in [mySentence1,mySentence2,mySentence3]:
            myText.to_edge(UP)
        self.play(Write(mySentence1))
        bullets= self.get_text_bullet(["¿Cuánta carga eléctrica hay en el universo?",
                                       "¿Cómo se distribuye?",
                                       "¿Cómo se comporta?"])
        bullets.next_to(mySentence1,DOWN)
        self.play(ShowIncreasingSubsets(bullets))
        self.wait(4)
        for myText in [mySentence2,mySentence3]:
            myText.set_width(config['frame_width'])
            self.play(Transform(mySentence1,myText))
        self.wait(6)
        self.play(ApplyWave(bullets))
        self.wait()
        self.get_function(bullets)
        self.wait()
    def get_text_bullet(self,text):
        blist= BulletedList(*text)
        blist.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        return blist
    def get_function(self, lista):
        square=Square().next_to(lista ,DOWN, buff=1)
        self.play(Create(square))
        self.play(
            ApplyPointwiseFunction(
                lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
                square
            )
        )
        self.wait()