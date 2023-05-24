from django.db import models

class CadExperience(models.Model):
    cadexperience_id = models.BigAutoField("ID", primary_key=True)
    cadexperience_first_name = models.CharField("NOME", max_length=50)
    cadexperience_last_name = models.CharField("SOBRENOME", max_length=50)
    cadexperience_degree = models.CharField("GRAU DE ESCOLARIDADE", max_length=2)

    def __str__(self) -> str:
        return self.cadexperience_first_name
