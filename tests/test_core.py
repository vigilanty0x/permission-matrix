import unittest
from permission_matrix.core import decide
class T(unittest.TestCase):
 def test_allow(self): self.assertEqual(decide("u","read","x",{"u":["r"]},[{"role":"r","action":"read","resource":"x","effect":"allow"}])["decision"],"allowed")
 def test_default(self): self.assertEqual(decide("u","read","x",{},[])["decision"],"denied")
 def test_deny_precedence(self): self.assertEqual(decide("u","read","x",{"u":["r"]},[{"role":"r","action":"*","resource":"*","effect":"allow"},{"role":"r","action":"read","resource":"x","effect":"deny"}])["decision"],"denied")
 def test_wildcard(self): self.assertEqual(decide("u","write","x",{"u":["r"]},[{"role":"r","action":"*","resource":"*","effect":"allow"}])["decision"],"allowed")
 def test_other_role(self): self.assertEqual(decide("u","read","x",{"u":["a"]},[{"role":"b","action":"read","resource":"x","effect":"allow"}])["decision"],"denied")
if __name__=="__main__": unittest.main()

