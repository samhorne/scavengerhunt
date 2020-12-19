from django.core.management.base import BaseCommand, CommandError
import clues.models as cModels
class Command(BaseCommand):
    help = 'Resets viewed status for all clues'

    def handle(self, *args, **options):
        qs = cModels.Clue.objects.all()
        qs.update(viewed_1=False, viewed_2=False)