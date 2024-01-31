import csv
import os
from calculator_app.models import Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import products from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        csv_file_path = os.path.abspath(csv_file_path)

        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                _, created = Product.objects.get_or_create(
                    name=row[1],
                    serving_size=row[2],
                    calories=row[3],
                    total_fat=row[4],
                    saturated_fat=row[5],
                    cholesterol=row[6],
                    sodium=row[7],
                    choline=row[8],
                    folate=row[9],
                    folic_acid=row[10],
                    niacin=row[11],
                    pantothenic_acid=row[12],
                    riboflavin=row[13],
                    thiamin=row[14],
                    vitamin_a=row[15],
                    vitamin_a_rae=row[16],
                    carotene_alpha=row[17],
                    carotene_beta=row[18],
                    cryptoxanthin_beta=row[19],
                    lutein_zeaxanthin=row[20],
                    lucopene=row[21],
                    vitamin_b12=row[22],
                    vitamin_b6=row[23],
                    vitamin_c=row[24],
                    vitamin_d=row[25],
                    vitamin_e=row[26],
                    tocopherol_alpha=row[27],
                    vitamin_k=row[28],
                    calcium=row[29],
                    copper=row[30],
                    iron=row[31],
                    magnesium=row[32],
                    manganese=row[33],
                    phosphorous=row[34],
                    potassium=row[35],
                    selenium=row[36],
                    zink=row[37],
                    protein=row[38],
                    alanine=row[39],
                    arginine=row[40],
                    aspartic_acid=row[41],
                    cystine=row[42],
                    glutamic_acid=row[43],
                    glycine=row[44],
                    histidine=row[45],
                    hydroxyproline=row[46],
                    isoleucine=row[47],
                    leucine=row[48],
                    lysine=row[49],
                    methionine=row[50],
                    phenylalanine=row[51],
                    proline=row[52],
                    serine=row[53],
                    threonine=row[54],
                    tryptophan=row[55],
                    tyrosine=row[56],
                    valine=row[57],
                    carbohydrate=row[58],
                    fiber=row[59],
                    sugars=row[60],
                    fructose=row[61],
                    galactose=row[62],
                    glucose=row[63],
                    lactose=row[64],
                    maltose=row[65],
                    sucrose=row[66],
                    fat=row[67],
                    saturated_fatty_acids=row[68],
                    monounsaturated_fatty_acids=row[69],
                    polyunsaturated_fatty_acids=row[70],
                    fatty_acids_total_trans=row[71],
                    alcohol=row[72],
                    ash=row[73],
                    caffeine=row[74],
                    theobromine=row[75],
                    water=row[76],
                )

        self.stdout.write(self.style.SUCCESS('Products imported successfully'))