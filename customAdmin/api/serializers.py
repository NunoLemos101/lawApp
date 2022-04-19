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
        arr = obj.title.split('-')
        if len(arr[1]) == 1:
            return arr[0] + " " + arr[1]
        elif len(arr[1]) == 2:
            return arr[0] + " " + arr[1][0]
        elif arr[0][len(arr[0]) - 1] == " ":
            return arr[0][:len(arr[0]) - 1]
        return arr[0]

    def get_title2(self, obj):
        try:
            title2 = obj.title.split('-')[1]
            print(title2)
            if len(title2) == 1:
                return obj.title.split('-')[2]
            elif len(title2) == 2:
                return obj.title.split('-')[2][1:]
            elif obj.title.split('-')[1][0] == " ":
                return obj.title.split('-')[1][1:]
            return obj.title.split('-')[1]

        except:
            if obj.title.split('-')[1][0] == " ":
                return obj.title.split('-')[1][1:]
            return obj.title.split('-')[1]
