# New import!
from django.db.models import Q


class FriendshipManager(models.Manager):
    def friends(self, user):
        """Get all users that are friends with the specified user."""
        # Get all friendships that involve the specified user.
        friendships = self.get_queryset().select_related(
            'user1', 'user2'
        ).filter(
            Q(user1=user) |
            Q(user2=user)
        )

        def other_user(friendship):
            if friendship.user1 == user:
                return friendship.user2
            return friendship.user1

        return map(other_user, friendships)