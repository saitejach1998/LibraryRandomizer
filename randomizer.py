import click

from JSONHandler import JSONHandler
from Indexer import Indexer
from helper import make_menu,randomize_video,play_video,draw_figlet



@click.command()
@click.option('-index','-i', is_flag=True, help="Indexes files in libraries")
def cli(index):
    """This is an CLI to randomize media playback from your media library."""

    if index or not(jhandler.ifIndexedLibraries()):
        indexDirs()

    Menu()


def Menu():

    draw_figlet()

    make_menu(jhandler.getIndexNames())

    input = click.prompt('What Would You like To See?', type=int)

    libobj = jhandler.getNthIndex(input)

    video_path = randomize_video(libobj)

    play_video(video_path,libobj)

def indexDirs():
    click.echo("Indexing Files....")
    libraries = jhandler.getLibs()
    indxer = Indexer(libraries)
    nols = indxer.index()
    click.echo("{} library items detected!".format(nols))
    click.echo("Done Indexing Files....")

if __name__ == "__main__":
    jhandler = JSONHandler()
    cli()
