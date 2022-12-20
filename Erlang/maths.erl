-module(maths).

-import(string, [len/1, concat/2, chr/2, substr/3, str/2, to_lower/1, to_upper/1]).

-export([main/0]).

main() ->
	{ok, Operate} = io:read("Enter the operation\n1.add\n2.sub\n3.mult\n4.div\n>>>"),
	{ok, A} = io:read("Enter a number >>>"),
	{ok, B} = io:read("Enter a number >>>"),
	case Operate of
		1 -> A + B;
		2 -> A - B;
		3 -> A * B;
		4 -> A / B
	end.

