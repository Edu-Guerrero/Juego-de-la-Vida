# Juego de la Vida

## Tabla de Contenidos
1. [Breve Explicación](#breve-explicación)
2. [Reglas](#reglas)
3. [Programa en Python](#programa-en-python)
   - [Librerías utilizadas](#librerías-utilizadas)
   - [Variables](#variables)
   - [Funciones](#funciones)
   - [Teclas](#teclas)
4. [English Version](#english-version)

## Breve Explicación

El Juego de la Vida es un autómata celular diseñado por el matemático británico John Horton Conway en 1970. Es un juego de cero jugadores, lo que significa que su evolución está determinada por su estado inicial, sin necesidad de intervención adicional. A pesar de su simplicidad, el Juego de la Vida puede simular una gran variedad de patrones complejos.

## Reglas

El juego se desarrolla en una cuadrícula de celdas, donde cada celda puede estar viva o muerta. La evolución de las celdas se rige por las siguientes reglas:

1. **Supervivencia**: Una celda viva con dos o tres vecinos vivos permanece viva para la siguiente generación.
2. **Muerte por soledad**: Una celda viva con menos de dos vecinos vivos muere en la siguiente generación.
3. **Muerte por sobrepoblación**: Una celda viva con más de tres vecinos vivos muere en la siguiente generación.
4. **Nacimiento**: Una celda muerta con exactamente tres vecinos vivos nace en la siguiente generación.

## Programa en Python

El script de Python crea el juego de la vida y permite ver cómo cambian los estados según los patrones dados.

### Librerías utilizadas

- **time**: Se usa `sleep` para pausar la ejecución y observar la evolución del juego.
- **pygame**: Se utiliza para crear la interfaz gráfica.
- **sys**: Se usa para salir del programa de manera segura.

### Variables

- `width`, `height`: Dimensiones de la ventana.
- `window`: Ventana del juego.
- `black`, `white`: Colores básicos.
- `option`: Selección de color.
- `color_options`: Lista de colores disponibles.
- `rows`, `cols`: Tamaño de la cuadrícula.
- `grid`, `next_grid`: Estado actual y futuro de la cuadrícula.

### Funciones

- `draw_grid()`: Dibuja la cuadrícula.
- `draw_cells()`: Dibuja las celdas.
- `get_cell_pos(mouse_pos)`: Obtiene la celda según el clic del usuario.
- `print_current_matrix()`: Imprime la matriz en consola.
- `analyze_matrix()`: Aplica las reglas del juego.
- `get_neighbors(row, col)`: Cuenta los vecinos vivos.
- `reset_grid()`: Reinicia la cuadrícula.

### Teclas

- **Click**: Marca una celda viva o muerta.
- **Tecla `c`**: Cambia el color de las celdas vivas.
- **Tecla `r`**: Reinicia la cuadrícula.
- **Tecla `espacio`**: Avanza un *tick*.
- **Tecla `Enter`**: Avanza automáticamente cada 0.5 segundos (se detiene con `Enter`).

## English Version

### Game of Life

#### Brief Explanation

The Game of Life is a cellular automaton created by British mathematician John Horton Conway in 1970. It is a zero-player game, meaning its evolution is determined by its initial state without further intervention. Despite its simplicity, the Game of Life can simulate a wide variety of complex patterns.

#### Rules

The game takes place on a grid where each cell can be alive or dead. The evolution of cells follows these rules:

1. **Survival**: A living cell with two or three living neighbors stays alive for the next generation.
2. **Underpopulation**: A living cell with fewer than two living neighbors dies.
3. **Overpopulation**: A living cell with more than three living neighbors dies.
4. **Reproduction**: A dead cell with exactly three living neighbors becomes alive.

### Python Program

The Python script creates the Game of Life and allows users to see how states change according to given patterns.

#### Libraries Used

- **time**: Uses `sleep` to pause execution and observe changes.
- **pygame**: Creates the graphical interface.
- **sys**: Safely exits the program.

#### Variables

- `width`, `height`: Window dimensions.
- `window`: The game window.
- `black`, `white`: Basic colors.
- `option`: Color selection.
- `color_options`: List of available colors.
- `rows`, `cols`: Grid size.
- `grid`, `next_grid`: Current and future grid states.

#### Functions

- `draw_grid()`: Draws the grid.
- `draw_cells()`: Draws the cells.
- `get_cell_pos(mouse_pos)`: Gets the clicked cell position.
- `print_current_matrix()`: Prints the grid in the console.
- `analyze_matrix()`: Applies game rules.
- `get_neighbors(row, col)`: Counts living neighbors.
- `reset_grid()`: Resets the grid.

#### Controls

- **Click**: Marks a cell as alive or dead.
- **Key `c`**: Changes the color of living cells.
- **Key `r`**: Resets the grid.
- **Key `space`**: Advances one *tick*.
- **Key `Enter`**: Advances automatically every 0.5 seconds (press `Enter` again to stop).

