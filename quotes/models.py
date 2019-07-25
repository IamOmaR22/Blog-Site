from django.db import models

# class QuoteCategory(models.Model):
#     title=models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.title

class Quote(models.Model):
    quote=models.TextField(max_length=200)
    author=models.CharField(max_length=50)
    title =models.CharField(max_length=50, null=True) # Must be null


    # quote_category=models.ForeignKey(
    #     'QuoteCategory',
    #     on_delete=models.CASCADE
    # )
    def __str__(self):
        if len(self.quote)> 50:
            return self.quote[:50]+"...."
        else:
            return self.quote