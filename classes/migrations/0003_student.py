from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_classroom_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=105)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('ml', 'male'), ('fl', 'female')], max_length=2)),
                ('exam_grade', models.IntegerField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Classroom')),
            ],
        ),
    ]