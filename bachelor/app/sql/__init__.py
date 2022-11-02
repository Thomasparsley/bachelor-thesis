from .gramar import statement_select, comment


sql = statement_select

sql.ignore(comment)

parse = sql.parse_string
