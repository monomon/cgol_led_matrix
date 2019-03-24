# Conway's Game of Life implementation and functions to display it on a led matrix screen using Raspberry Pi

The main implementation is in cgol.py
You can use it like so:

    import cgol
    play(cgol.glider)

## Example

The library mostly works with two-dimensional arrays of 0s and 1s representing the world state.

    glider2 = cgol.get_next_grid(cgol.glider)

## Functions

**cgol.play(initial_grid)**

displays the state on stdout and clears the screen between frames

**cgol.get_next_state(cell, neighborhood)**

is the core function that implements the rules of Game of Life.
It decides whether a cell will live, depending on its own state and its neighbors'.

**cgol.get_neighborhood(grid, width, height, pos)**

get the neighborhood of a cell at a given position

## Patterns

**cgol.glider**

8x8 array initialized to contain one glider.

**cgol.beacon**

8x8 array initialized to contain a beacon pattern.

**cgol.diehard**

8x8 array containing a diehard pattern.
