from django.db import models


class Section(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    items = models.ForeignKey('Item', on_delete=models.CASCADE)

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'items': [item.serialize() for item in self.items]
        }


class Item(models.Model):
    id = models.IntegerField(primary_key=True, )
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    section_id = models.IntegerField(models.ForeignKey('section.id', on_delete=models.CASCADE))
    modifiers = models.ForeignKey('Modifier', on_delete=models.CASCADE)

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'modifiers': [item.serialize() for item in self.modifiers]
        }


class Modifier(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=10000)
    items = models.ForeignKey('Item', on_delete=models.CASCADE)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.description
        }


class Side(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField(models.ForeignKey('item.id', on_delete=models.CASCADE))
    modifier_id = models.IntegerField(models.ForeignKey('modifier.id', on_delete=models.CASCADE))
