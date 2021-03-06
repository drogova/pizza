import click

@click.group()
def cli():
    pass

@cli.command()
@click.option(' delivery',default=False,is_flag=True)
@click.argument('pizza',nargs=1)
def bake(pizza:str,delivery:bool):
    print(pizza, delivery)

@cli.command()
def menu():
    print('Наши пиццы!')

if __name__ == '__main__'
    cli()