NAME 	= step2

SRC 	= main.c

OBJ 	= $(SRC:.c=.o)

CC 	= gcc -o $(NAME) -g3

RM 	= rm -f

$(NAME):
	$(CC) $(SRC)

all: 	$(NAME)

clean:
	$(RM) $(OBJ)

fclean: clean
	$(RM) $(NAME)

re: 	fclean all

.PHONY: all clean fclean re
