# DjangoAbstractUserEmailLoginBased
Exemple d'implémentation de Abstract User de Djando avec identification avec email aulieu de username

## Procédure
### Les Modeles
Premièrement :
  - Créer dans votre model.py une classe User (ici NotreUser) qui hérite de AbstractUser
  
  ```py 
class NotreUser(AbstractUser):
        pass
```
      
 Deuxiemement :
 
 - Lier le User model avec notre class metier (ici Etudiant)
  
```py
class Etudiant(models.Model):
    user = models.OneToOneField(NotreUser,on_delete=models.CASCADE)
```    
Troisièmement :
  - Ajouter notre User model comme class d'adminitration
```py
admin.register(NotreUser)

class MyUserAdmin(UserAdmin):
    pass
```    
Enfin :
  - Faire la migration
  
   ```sh
$ python manage.py makemigrations
$ python manage.py migrate
```
  
  
### Les Formulaires
    Il nous faudra associé nos class avec des Formulaires afin de simplifier leur insertion en base de donnée 
Premièrement :
  - Créer le formulaire de notre User Model, notre formulaire hérite de UserCreationForm
    * On lui indique aussi le type de notre model ici (NotreUser)
    * On lui indique aussi les champs à afficher (ici nous avons l'email,le prenom,etc...)
  ```py
class NotreUserCreationForm(UserCreationForm):
    class Meta:
        model = NotreUser
        fields = ("email","first_name","last_name","is_sick")
```   
Deuxiement : 
  -Créer le formulaire de notre class métier (ici Etudiant)
  
   ```py
class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        exclude = ("user",)
```   
  

   ```sh
$ npm install --production
$ npm run predeploy
$ NODE_ENV=production node app
```
