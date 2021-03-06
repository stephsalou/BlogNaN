from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import Categorie, Article, Tag, Commentaire, ResponseCommentaire, Like, DisLike, DemandeAdesion
from Utilisateurs.models import MyUser

class LikeSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Like
        fields= '__all__'
        
class DisLikeSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = DisLike
        fields= '__all__'
        
class DemandeAdesionSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = DemandeAdesion
        fields= '__all__'
        
class ResponseCommentaireSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = ResponseCommentaire
        fields= '__all__'
        
class CommentaireSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    response = ResponseCommentaireSerializer(many=True, required=False)
    class Meta:
        model = Commentaire
        fields= '__all__'
        depth = 1
        
# class ArchiveSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
#     class Meta:
#         model = Archive
#         fields= '__all__'
        
class ArticleSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    article_commentaire = CommentaireSerializer(many=True, required=False)
    # archive_article = ArchiveSerializer(many=True, required=False)
    article_like = LikeSerializer(many=True, required=False)
    Dislike = DisLikeSerializer(many=True, required=False)    
    class Meta:
        model = Article
        fields= '__all__'
        depth = 1        
        
class TagSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    article_tag = ArticleSerializer(many=True, required=False)
    class Meta:
        model = Tag
        fields= '__all__'
        depth = 1
        
class UserSerializer(serializers.ModelSerializer):
    article_auteur = ArticleSerializer(many=True, required=False)
    user_comment = CommentaireSerializer(many=True, required=False)
    user_response_comment = ResponseCommentaireSerializer(many=True, required=False)
    user_like = LikeSerializer(many=True, required=False)
    user_dislike = DisLikeSerializer(many=True, required=False)
    user_demande = DemandeAdesionSerializer(many=True, required=False)
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        depth = 1
        
    def create(self, validated_data):
        user = MyUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
class CategorieSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    article_categorie = ArticleSerializer(many=True, required=False)
    class Meta:
        model = Categorie
        fields= '__all__'
        depth = 1