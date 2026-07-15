# format values based on flags inserted {value:flags}
# .2f means to format the value as a float with 2 decimal places
# > means to align the value to the right
# < means to align the value to the left
# ^ means to align the value to the center
# 0 means to fill the empty space with 0
# any number means to fill the empty space with that number of spaces meaing give me 10 places to display the value
# + means to show the sign of the number or you can use an empty space to show the sign of the number
# , means to format the number with a comma as a thousands separator
# you can combine multiple flags together to format the value in a specific way


price = 49.99123213
formatted_price = f"{price:.2f}"  # format the price to 2 decimal places which is 49.99

price2 = 49.99123213
price3= -5555.21312
formatted_price2 = f"{price2:+}"  # format the price to show the sign which is +49.99123213
formatted_price3 = f"{price3:+}"  # have no effect on -ve numbers but will show the sign for +ve numbers which is -5555.21312

format_price4 = f"{price2:>10.2f}"  # format the price to 2 decimal places and align it to the right with 10 spaces which is '    49.99'
format_price5 = f"{price2:<10.2f}"  # format the price to 2 decimal places and align it to the left with 10 spaces which is '49.99    '
format_price6 = f"{price2:^10.2f}"  # format the price to 2 decimal places and align it to the center with 10 spaces which is '  49.99   '

format_price7 = f"{price2:0>10.2f}"  # format the price to 2 decimal places and align it to the right with 10 spaces and fill the empty space with 0 which is '000049.99'
