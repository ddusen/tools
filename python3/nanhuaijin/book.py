import ebooklib
from ebooklib import epub


def main():
	file_path = '/Users/dusen/Documents/book/南怀瑾套装52册/南怀瑾著作全收录（套装共52册）/南怀瑾著作全收录（套装共52册）.epub'
	book = epub.read_epub(file_path)

	new_book = epub.EpubBook()

	for item in book.get_items():
	    if item.get_type() == ebooklib.ITEM_DOCUMENT:
	    	item_name = item.get_name()
	    	if item_name >= 'part0001.xhtml' and item_name < 'part0028.xhtml':
	    		new_book.add_item(item.get_context())

	# TODO: somethings...
	epub.write_epub('论语别裁.epub', new_book, {})


def item_dict():
	return {
		'part0001.xhtml': '论语别裁',
		'part0028.xhtml': '话说中庸',
		'part0040.xhtml': '原本大学微言',
		'part0056.xhtml': '金刚经说什么',
		'part0098.xhtml': '孟子旁通',
		'part0108.xhtml': '孟子与万章',
		'part0115.xhtml': '孟子与离娄',
		'part0122.xhtml': '孟子与公孙丑',
		'part0129.xhtml': '孟子与尽心篇',
		'part0136.xhtml': '孟子与滕文公、告子',
		'part0144.xhtml': '我说《参同契》（上册）',
		'part0176.xhtml': '我说《参同契》（中册）',
		'part0207.xhtml': '我说《参同契》（下册）',
		'part0239.xhtml': '维摩诘的花雨满天（上册）',
		'part0247.xhtml': '维摩诘的花雨满天（下册）',
		'part0259.xhtml': '列子臆说',
		'part0289.xhtml': '列子臆说',
		'part0322.xhtml': '列子臆说',
		'part0352.xhtml': '瑜伽师地论',
		'part0377.xhtml': '廿一世纪初的前言后语',
		'part0398.xhtml': '漫谈中国文化',
		'part0406.xhtml': '禅与生命的认知初讲',
		'part0419.xhtml': '小言黄帝内经与生命科学',
		'part0433.xhtml': '庄子諵譁',
		'part0446.xhtml': '人生的起点和终站',
		'part0454.xhtml': '南怀瑾与彼得圣吉',
		'part0460.xhtml': '老子他说：初续合集',
		'part0470.xhtml': '答问青壮年参禅者',
		'part0480.xhtml': '南怀瑾讲演录',
		'part0490.xhtml': '中国道教发展史略述',
		'part0505.xhtml': '中国佛教发展史略述',
		'part0516.xhtml': '新旧教育的变与惑',
		'part0544.xhtml': '易经系传别讲',
		'part0551.xhtml': '易经杂说',
		'part0722.xhtml': '静坐修道与长生不老',
		'part0782.xhtml': '禅话',
		'part0803.xhtml': '药师经的济世观',
		'part0944.xhtml': '历史的经验',
		'part0999.xhtml': '中国文化泛言增订本',
		'part1010.xhtml': '禅海蠡测',
		'part1043.xhtml': '如何修证佛法',
		'part1081.xhtml': '孔子和他的弟子们',
		'part1094.xhtml': '大圆满禅定休息简说',
		'part1118.xhtml': '禅宗与道家',
		'part1128.xhtml': '定慧初修',
		'part1143.xhtml': '楞严大义今释',
		'part1162.xhtml': '圆觉经略说',
		'part1183.xhtml': '学佛者的基本信念'
	}

if __name__ == '__main__':
	main()
