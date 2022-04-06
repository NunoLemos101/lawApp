from rest_framework import serializers
from customAdmin.models import DailyStatistics
from notes.models import Article


class DailyStatisticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyStatistics
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['title', 'id']


class ReactNativeArticlesSerializer(serializers.ModelSerializer):

    title1 = serializers.SerializerMethodField()
    title2 = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ["title1", "title2", "id"]

    def get_title1(self, obj):
        return obj.title.split('-')[0]

    def get_title2(self, obj):
        try:
            title2 = obj.title.split('-')[1]
            return title2
        except:
            return obj.title.split('-')[0]
