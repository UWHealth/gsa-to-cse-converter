from xml.sax.saxutils import escape
import sys, csv

def make_xml_string(csv_file):
	start = \
	'<?xml version="1.0" encoding="UTF-8"?>\n\
	<Promotions start="0" num="%(promotion_count)s" total="%(promotion_count)s">\n'
	promotion = \
	'	<Promotion queries="%(queries)s" title="%(title)s" url="%(url)s"/>\n'
	end = \
	'</Promotions>'

	promo_lines = []
	for row in csv_file:
		c = {
			"queries": escape(row[0].rstrip('\r\n')),
			"url": escape(row[2].rstrip('\r\n')),
			"title": escape(row[3].rstrip('\r\n'))
		}
		if (c['queries'] and c['url'] and c['title']):
			promo_lines.append(promotion % c)
		else:
			print(line);
	return start % {"promotion_count":len(promo_lines)} + "".join(promo_lines) + end


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
        csv_file = csv.reader(open(file_name, 'r+'))
        print (make_xml_string(csv_file))
    except IndexError:
        print ("Usage: gsa-to-cse.py <input_file.csv>")
        sys.exit(1)
