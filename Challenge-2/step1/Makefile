NAME    = step1

SRC     = main.c

OBJ     = $(SRC:.c=.o)

CC      = gcc -o $(NAME)

RM      = rm -f

$(NAME):
	$(CC) $(SRC)

all:    $(NAME)

debug:  $(CC) -g3

clean:
	$(RM) $(OBJ)

fclean: clean
	$(RM) $(NAME)

re:     fclean all

.PHONY: all clean fclean re

