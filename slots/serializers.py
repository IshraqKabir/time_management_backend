from rest_framework import serializers
from .models import Slot
from tasks.models import Task

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.day = validated_data.get('day', instance.day)
        instance.month = validated_data.get('month', instance.month)
        instance.year = validated_data.get('year', instance.year)
        instance.start_time_hours = validated_data.get('start_time_hours', instance.start_time_hours)
        instance.start_time_mins = validated_data.get('start_time_mins', instance.start_time_mins)
        instance.end_time_hours = validated_data.get('end_time_hours', instance.end_time_hours)
        instance.end_time_mins = validated_data.get('end_time_mins', instance.end_time_mins)
        instance.is_done = validated_data.get('is_done', instance.is_done)
        instance.is_added = validated_data.get('is_added', instance.is_added)
        instance.task = validated_data.get('task', instance.task)

        if instance.is_done and instance.is_added==False:
            [total_time_hours, total_time_mins]  = instance.task.total_time_done.split(':')
            total_time_hours = int(total_time_hours)
            total_time_mins = int(total_time_mins)
            print('total_time_hours')
            print(total_time_hours)
            print('total_time_mins')
            print(total_time_mins)
            total_time_length_mins = total_time_hours*60 + total_time_mins
            print('total_time_length_mins')
            print(total_time_length_mins)

            # slot times
            slot_start_hours = instance.start_time_hours
            slot_start_mins = instance.start_time_mins
            print('slot_start_hours')
            print(slot_start_hours)
            print('slot_start_mins')
            print(slot_start_mins)
            slot_end_hours = instance.end_time_hours
            slot_end_mins = instance.end_time_mins
            print('slot_end_hours')
            print(slot_end_hours)
            print('slot_end_mins')
            print(slot_end_mins)
            slot_length_mins = (slot_end_hours - slot_start_hours)*60 + (slot_end_mins-slot_start_mins)
            print('slot_length_mins')
            print(slot_length_mins)
            final_time_mins = slot_length_mins + total_time_length_mins
            print("finl tme mins")
            print(final_time_mins)
            final_time = f'{final_time_mins//60}:{final_time_mins%60}'
            # Task.objects.filter(id=instance.task.id).update(total_time_done=final_time)
            if instance.task.project:
                print(instance.task.project.name)
            else:
                print('no project of this take')
            instance.is_added = True
        return instance
        