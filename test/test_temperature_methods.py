import unittest
from custom_functions import temperature_methods

class TestCollectionMethods(unittest.TestCase):
    def  test_promedio(self):
        dic={"enero":-12,"febrero":12,"marzo":-12,"abril":12,"mayo":-12,"junio":12,"julio":-12,"agosto":12,"septiembre":-12,"octubre":12,"noviembre":-12,"diciembre":12}
        promedio=temperature_methods.prom1(dic)
        self.assertEqual(promedio, 0)

    def test_promedio1(self):
        dic1={"enero":0,"febrero":0,"marzo":0,"abril":0,"mayo":0,"junio":0,"julio":0,"agosto":0,"septiembre":0,"octubre":0,"noviembre":0,"diciembre":0}
        promedio1 = temperature_methods.prom1(dic1)
        self.assertEqual(promedio1, 0)

    def test_promedio2(self):
        dic2={"Enero":3}
        promedio2 = temperature_methods.prom1(dic2)
        self.assertEqual(promedio2, 3)




