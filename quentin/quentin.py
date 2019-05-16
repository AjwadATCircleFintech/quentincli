import sys
import os
import random
import click

# Adding directory to the path
sys.path.append(os.path.dirname(os.path.realpath(__file__)))


def goodbye():
    """
    Exits with a user friendly greeting
    """
    click.echo('\nThanks for using Quentin CLI. Have a great day!\n')
    sys.exit()


def dummy_search(search_str):
    """
    Takes the search_str input and returns a mock results list
    """
    quentin_movies = ['Pulp Fiction', 'Django Unchained', 'The Hateful Eight', 'True Romance', 'Sin City', 'Reservoir Dogs', 'Kill Bill']
    return quentin_movies[ : random.randrange(3, len(quentin_movies))]


def dummy_process(results_list, idx_list):
    """
    Prints the selections made by the user
    """
    if not idx_list:
        click.echo("\nYou have made no selections. Ending the session.\n")
        goodbye()

    click.echo("\nYour selected results are as follows:")
    for i in idx_list:
        click.echo(f"\t{results_list[i]}")
    click.echo()

@click.command(name='quentin-cli')
@click.help_option('-h', '--help')
@click.version_option(version='v0.1', prog_name='quentin-cli')
def cli():
    """
    Quentin CLI

    "Do you know what this is? It’s the world’s smallest violin playing just for the waitresses."
    """
    # Prompt for and process the search string
    search_str = click.prompt('> Please enter a search string\n')
    results_list = dummy_search(search_str)
    results_len = len(results_list)

    # Handle scenario with no search result matches
    if not results_list:
        click.echo(f"Sorry, no results were found for '{search_str}'. Please try again with a different search string.")
        sys.exit()

    # Print search results
    click.echo(f"\nYou have entered '{search_str}' as a search string. Below are the results:")
    for idx, val in enumerate(results_list):
        click.echo(f'\t{idx}. {val.title()}')
    click.echo()

    selection_prompt = '> Please select results using by specifying the indices, one selection at a time\n'

    selected_indices = []

    while True:
        selection = click.prompt(selection_prompt)

        # Check for exiting or ending selection
        if selection in ['exit', 'done']:
            confirm_resp = click.confirm(f"> You have entered '{selection}'. Are you certain of your choice?")

            # Check for exit trigger
            if confirm_resp and selection == 'exit':
                click.echo("\nYou have chosen to end the session.\n")
                goodbye()

            # Check for batch processing trigger
            elif confirm_resp:
                click.echo("\nYou have chosen to process your selection.\n")
                dummy_process(results_list, selected_indices)
                break

        try:
            selection_idx = int(selection)

            # Check for valid index
            if selection_idx >= 0 and selection_idx < results_len and selection_idx not in selected_indices:
                selected_indices.append(selection_idx)
            else:
                click.echo("\nYou have provided an invalid index. Please select unique indices from the given range.\n")

        # Handle a non integer value that doesn't fall in the accepted strings list
        except ValueError:
            click.echo("\nYou have provided an invalid string. Enter 'done' to start processing or 'exit' to end the session, or continue selection.\n")

    click.echo("\nYour selection has been processed.\n")
    goodbye()

if __name__ == '__main__':
    cli()
