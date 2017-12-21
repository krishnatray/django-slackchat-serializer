# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 15:06
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_tag', models.SlugField(max_length=255)),
                ('character', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.SlugField(blank=True, editable=False, max_length=10, null=True)),
                ('name', models.CharField(blank=True, editable=False, max_length=150, null=True)),
                ('owner', models.CharField(choices=[('U1SPM8DC0', 'aabril@politico.com'), ('U28R24K1C', 'aadragna@politico.com'), ('U2RMM881Y', 'abehsudi@politico.com'), ('U301T5ATU', 'acancryn@politico.com'), ('U4U8L8JUB', 'ahurst@politico.com'), ('U2ZJSDJUD', 'agreilingkeane@politico.com'), ('U2K6K7S4W', 'ahanna@politico.com'), ('U3TC14MEK', 'ahoffman@politico.com'), ('U0AN43XCH', 'aisenstadt@politico.com'), ('U2QUJGMNJ', 'ajakabcin@politico.com'), ('U081UE9C0', 'akarni@politico.com'), ('U6KS7CBV3', 'alacy@politico.com'), ('U37NZ0849', 'avelickovich@politico.com'), ('U0BTDEKLH', 'aguillen@politico.com'), ('U439APEE7', 'aphelps@politico.com'), ('U1VSTAGJV', 'athorne@politico.com'), ('U0BJVM7E0', 'agoodwin@politico.com'), ('U1MF077LK', 'astubbs@politico.com'), ('U0L1545UY', 'apalmer@politico.com'), ('U0BTA2GKX', 'arestuccia@politico.com'), ('U0FHGMZ4K', 'asnider@politico.com'), ('U2ZMG3S2F', 'aweaver@politico.com'), ('U6W564BCM', 'bbecker@politico.com'), ('U0NS8TMAB', 'bdayspring@politico.com'), ('U464U0N78', 'blefebvre@politico.com'), ('U2ANMR2US', 'bweyl@politico.com'), ('U0AP1C5NE', 'bwhite@politico.com'), ('U2BA099NV', 'bgriffiths@politico.com'), ('U113DBRBK', 'bgurciullo@politico.com'), ('U2RLNMEUR', 'bhillman@politico.com'), ('U1F3P2X2Q', 'bpadro@politico.com'), ('U0CHY31KR', 'bduryea@politico.com'), ('U0C2LLUH2', 'bkuchman@politico.com'), ('U0ALHHQBU', 'bking@politico.com'), ('U04CVTYKA', 'bhounshell@politico.com'), ('U4JCNVDC7', 'bmacarthur@politico.com'), ('U198YQCGY', 'beverett@politico.com'), ('U0A4SEGD9', 'bpeterson@politico.com'), ('U2N69NF2L', 'bqatipi@politico.com'), ('U0944177F', 'behley@politico.com'), ('U0ANB6GQ2', 'bmulcahy@politico.com'), ('U301PTEEQ', 'britchie@politico.com'), ('U304P9CJH', 'bwermund@politico.com'), ('U0X91BK5J', 'coconnell@politico.com'), ('U2ZRESPDG', 'coprysko@politico.com'), ('U2LSVQ4FP', 'csandstrom@politico.com'), ('U1SQEGZ24', 'ckelly@politico.com'), ('U2YP3RKPW', 'cbrown@politico.com'), ('U15B2SW6P', 'cbaute@politico.com'), ('U2YUKJ84U', 'cbudoff@politico.com'), ('U4HGYBCR1', 'cbrownell@politico.com'), ('U0AQY8545', 'cemma@politico.com'), ('U5N08DWD8', 'cfoxwell@politico.com'), ('U0607KKA4', 'cmahtesian@politico.com'), ('U6Z6947B2', 'ckarna@politico.com'), ('U0AQFE4KS', 'cbenson@politico.com'), ('U178FC98D', 'clima@politico.com'), ('U1TH6E94J', 'cobrien@politico.com'), ('U0AQVKWG5', 'cwilhelm@politico.com'), ('U2M6CK0DR', 'cbennett@politico.com'), ('U09EX4ZLG', 'chowie@politico.com'), ('U0LP8J2P4', 'cschneier@politico.com'), ('U38NANURX', 'dbishop@politico.com'), ('U06JPATP1', 'dstrauss@politico.com'), ('U0AQZ7448', 'dvinik@politico.com'), ('U1EUY2ZQ8', 'dspinelli@politico.com'), ('U09HL8GSK', 'dcohen@politico.com'), ('U084VCHSS', 'ddabruzzo@politico.com'), ('U1SS3J952', 'ddiamond@politico.com'), ('U0BTG4U57', 'ddixon@politico.com'), ('U2YMUBL80', 'dducassi@politico.com'), ('U5TAQBHT7', 'daurelius@politico.com'), ('U0NAMU8S3', 'bbender@politico.com'), ('U09CDS23W', 'dkihara@politico.com'), ('U07V2P7DW', 'dlippman@politico.com'), ('U1EV3DT9Q', 'dharrell@politico.com'), ('U3TNJ51C2', 'dpalmer@politico.com'), ('U7167DFAL', 'drobertson@politico.com'), ('U0ANFSDF0', 'dsamuelsohn@politico.com'), ('U09HDQPEJ', 'eschneider@politico.com'), ('U1SPGL1RS', 'edobler@politico.com'), ('U0AQN8J20', 'eengleman@politico.com'), ('U6H65M171', 'eholden@politico.com'), ('U0AP412SC', 'ceisenberg@politico.com'), ('U36UAFTF0', 'ejohnson@politico.com'), ('U09UDM00Y', 'eralph@politico.com'), ('U69LA48BA', 'egoldberg@politico.com'), ('U4R16RK53', 'estephenson@politico.com'), ('U2MT2TJJD', 'egeller@politico.com'), ('U0BTAG7FA', 'ewolff@politico.com'), ('U51ACPMHQ', 'eriley@politico.com'), ('U0LKACSQM', 'eaulov@politico.com'), ('U0BTCMKD3', 'eschor@politico.com'), ('U07TUTP16', 'gdebenedetti@politico.com'), ('U4M1RFUHJ', 'gbrotman@politico.com'), ('U720TJXA9', 'gglatsky@politico.com'), ('U4HH5Q6H1', 'ggoodman@politico.com'), ('U07V86U02', 'hjackson@politico.com'), ('U1B64GTFT', 'hcaygle@politico.com'), ('U2G6R9VFD', 'ikullgren@politico.com'), ('U2G8EP16C', 'isaac@politico.com'), ('U2LQ299RV', 'jheinz@politico.com'), ('U130UQ0EQ', 'jsmith@politico.com'), ('U1819GV42', 'jsherman@politico.com'), ('U1GTY36RG', 'jamster@politico.com'), ('U0AQ1PHGX', 'jmillman@politico.com'), ('U0LRG5D9B', 'jbresnahan@politico.com'), ('U1FHQQRFX', 'jcuellar@politico.com'), ('U5PGG84PP', 'jlin@politico.com'), ('U30JE92G5', 'jblount@politico.com'), ('U0AQXQF0X', 'jhaberkorn@politico.com'), ('U7E5R7A2G', 'jklimas@politico.com'), ('U56DEADT9', 'jmichaud@politico.com'), ('U4HMKDDNZ', 'jmiller@politico.com'), ('U0ANY3D43', 'jkenen@politico.com'), ('U1DPMRWHL', 'jlauinger@politico.com'), ('U4XV32XKR', 'jmcclure@politico.com'), ('U5GUJNRPX', 'jhalling@politico.com'), ('U0BH0V25R', 'jgerstein@politico.com'), ('U5RGFNUTH', 'jmeyer@politico.com'), ('U50NR064T', 'jplesniak@politico.com'), ('U0AQVA6ES', 'jscholtes@politico.com'), ('U6V6HGR2P', 'jschwartz@politico.com'), ('U2LR2CHR9', 'jzbenson@politico.com'), ('U04RJGPT5', 'kareywutkowski@gmail.com'), ('U13JDSSKA', 'kmckibben@politico.com'), ('U2ZMJ6RRB', 'klandergan@politico.com'), ('U497JU6KF', 'kmoukhina@politico.com'), ('U0BJZGKDW', 'kbarnard@politico.com'), ('U1SPSSKEZ', 'kburton@politico.com'), ('U07UQH5NV', 'kcheney@politico.com'), ('U0AN64CLU', 'keast@politico.com'), ('U09GTA39V', 'krobillard@politico.com'), ('U0AMS55RS', 'kfossett@politico.com'), ('U0APZM2CE', 'khefling@politico.com'), ('U1SPJ7K9S', 'kmiller@politico.com'), ('U4GB9N0JZ', 'kpudwill@politico.com'), ('U2LSW1971', 'krector@politico.com'), ('U75FQ4PQA', 'krice@politico.com'), ('U5ZKPKYRE', 'ktamborrino@politico.com'), ('U0PGV8WQ7', 'kodonnell@politico.com'), ('U3D664FML', 'kwyatt@politico.com'), ('U2ZLYL8JH', 'ldezenski@politico.com'), ('U2M81FX5F', 'lgardner@politico.com'), ('U4XSAAAH3', 'lmihalik@politico.com'), ('U2MDKHCDV', 'lmertz@politico.com'), ('U2QRVQ6P5', 'lli@politico.com'), ('U3GPCLXPF', 'lmonaghan@politico.com'), ('U3BT4V483', 'lmuntzing@politico.com'), ('U2M7Z20MT', 'lwoellert@politico.com'), ('U09E71A85', 'lnelson@politico.com'), ('U6Z0YLEA0', 'lsanchez@politico.com'), ('U0CAP3QRW', 'mseverns@politico.com'), ('U0A051TCJ', 'mslattery@politico.com'), ('U30E4RVK8', 'mmatishak@politico.com'), ('U0AQQBENS', 'mdaily@politico.com'), ('U0QNU6989', 'mnussbaum@politico.com'), ('U0C2M90R2', 'mbloom@politico.com'), ('U770N1KKQ', 'mcalderone@politico.com'), ('U4BSQ51T7', 'mcassella@politico.com'), ('U0AN6DFU2', 'mcrowley@politico.com'), ('U2LTDP1BK', 'michellez@politico.com'), ('U0800UDKJ', 'mzapler@politico.com'), ('U1HGCCF71', 'mirwin@politico.com'), ('U0HAATT9N', 'mschuler@politico.com'), ('U0AMXDNKW', 'mkady@politico.com'), ('U1SPSEDK9', 'mlee@politico.com'), ('U2RM8UHL6', 'mleonor@politico.com'), ('U2RM777JL', 'mlevine@politico.com'), ('U09R4G4EM', 'mreynolds@politico.com'), ('U0NT2MQE9', 'mswiatkowski@politico.com'), ('U54A64Z4K', 'nfreiberg@politico.com'), ('U0AQVA1DY', 'njuliano@politico.com'), ('U1W37ACQ4', 'nnarea@politico.com'), ('U0E7MP405', 'nmccaskill@politico.com'), ('U0AN62LR0', 'ntoosi@politico.com'), ('U0AQSD4HW', 'pcanellos@politico.com'), ('U5MD6AFFB', 'pjoshi@politico.com'), ('U0PQAF7K3', 'ptemple-west@politico.com'), ('U3B0ZV8KE', 'pvolpe@politico.com'), ('U0AQ90A4F', 'rpradhan@politico.com'), ('U30Q7KXQW', 'rarrieta-kenna@politico.com'), ('U1X48QNSE', 'rshamon@politico.com'), ('U0BK1C1QU', 'rbade@politico.com'), ('U49LANBQB', 'rflores@politico.com'), ('U6CCB91AM', 'rlemmerman@politico.com'), ('U1M105C72', 'rmorin@politico.com'), ('U6RK9984U', 'rrobinson@politico.com'), ('U0BJVV3HR', 'rturner@politico.com'), ('U5GTA0H6Y', 'sbarnes@politico.com'), ('U5SFBECBS', 'sfrostenson@politico.com'), ('U8DFBLWPL', 'sbeynon@politico.com'), ('U2Z6AV6SJ', 'sbustos@politico.com'), ('U0E8GMTFU', 'sbland@politico.com'), ('U4HK8H4CB', 'seppler@politico.com'), ('U198EQDG9', 'skim@politico.com'), ('U0AN15WJ0', 'sheuser@politico.com'), ('U4BC16USV', 'slackadmin@politico.com'), ('U6S00T63C', 'smajid@politico.com'), ('U09R2KN7R', 'msobocinski@politico.com'), ('U2LSL5K1N', 'swillis@politico.com'), ('U38EZ7FEW', 'srafferty@politico.com'), ('U09HENNDB', 'sshepard@politico.com'), ('U3LRDATQA', 'sreddy@politico.com'), ('U2R3FNQAH', 'scagle@politico.com'), ('U0BJXRA95', 'ssagar@politico.com'), ('U2U3NBQLT', 'tsnyder@politico.com'), ('U6XTN00QH', 'tthomas@politico.com'), ('U28LCU7MF', 'tgee@politico.com'), ('U0V3PC43F', 'tdoherty@politico.com'), ('U2RMS9482', 'thesson@politico.com'), ('U09E8G563', 'tmeyer@politico.com'), ('U6SBQQ86R', 'tlindeman@politico.com'), ('U073DEM1B', 'teischen@politico.com'), ('U2RL0NL31', 'tsperling@politico.com'), ('U30NKLTSS', 'tstarks@politico.com'), ('U2LSQK9TP', 'tweyant@politico.com'), ('U1GT60ZMF', 'tpager@politico.com'), ('U5U0DHNB1', 'tfisher@politico.com'), ('U2ZJ3P8AH', 'vguida@politico.com'), ('U2LT1TYVC', 'whouseknecht@politico.com'), ('U5V8MKTV5', 'jyuan@politico.com'), ('U0PQ4TK5E', 'zwarmbrodt@politico.com'), ('U0Y57RBRB', 'zmontellaro@politico.com'), ('U0USU8V0B', 'zstanton@politico.com')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ChatType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MarkupContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(unique=True)),
                ('text', models.TextField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='slackchat.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='MessageMarkup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=255)),
                ('search_string', models.CharField(max_length=255)),
                ('regex', models.BooleanField(default=False)),
                ('action_tag', models.SlugField(max_length=255)),
                ('flow', models.CharField(choices=[('I', 'In flow'), ('O', 'Out of flow'), ('B', 'Both')], default='I', max_length=1)),
                ('content_template', django.contrib.postgres.fields.jsonb.JSONField()),
                ('chat_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slackchat.ChatType')),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(unique=True)),
                ('reaction', models.CharField(max_length=150)),
                ('action', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='slackchat.Action')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='slackchat.Message')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(unique=True)),
                ('key', models.SlugField(max_length=30)),
                ('value', models.TextField()),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slackchat.Message')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('chat_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='slackchat.ChatType')),
            ],
        ),
        migrations.CreateModel(
            name='RoleAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.CharField(max_length=50)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='roleassignment',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='slackchat.User'),
        ),
        migrations.AddField(
            model_name='roleassignment',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='slackchat.Channel'),
        ),
        migrations.AddField(
            model_name='roleassignment',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='slackchat.Role'),
        ),
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slackchat.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='slackchat.User'),
        ),
        migrations.AddField(
            model_name='markupcontent',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slackchat.Message'),
        ),
        migrations.AddField(
            model_name='markupcontent',
            name='message_markup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slackchat.MessageMarkup'),
        ),
        migrations.AddField(
            model_name='channel',
            name='chat_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slackchat.ChatType'),
        ),
        migrations.AddField(
            model_name='action',
            name='chat_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slackchat.ChatType'),
        ),
        migrations.AddField(
            model_name='action',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='slackchat.Role'),
        ),
    ]
