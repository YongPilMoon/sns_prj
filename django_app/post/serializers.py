from rest_framework import serializers

from post.models import Comment
from post.models import Post, HashTag, PostLike, PostBookMark


class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = ('name',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'post', 'author', 'modified_date')


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'content',
            'author',
            'created_date',
            'modified_date',
            'like_users_counts',
            'comments_counts',
            'distance'
            )


class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')
    hashtags = HashTagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'content', 'author', 'created_date', 'modified_date', 'view_counts',
                  'like_users_counts', 'distance','is_bookmarked', 'comments_counts', 'hashtags', 'comments')


class PostCreateSerializer(serializers.ModelSerializer):
    hashtags = HashTagSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'content', 'author', 'hashtags')

    def create(self, validated_data):
        hashtags = validated_data.pop('hashtags')
        post = Post.objects.create(**validated_data)
        if hashtags != None:
            for hashtag in hashtags:
                h, created = HashTag.objects.get_or_create(name=hashtag)
                post.hashtags.add(h)
        return post


class PostLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostLike
        fields = ('like_user', 'post')


class PostBookMarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostBookMark
        fields = ('bookmark_user', 'post')

