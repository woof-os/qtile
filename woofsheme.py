class ColorScheme():
	def __init__(self, bg, fg, **kwargs):
		self.bg = bg
		self.fg = fg
		self.__dict__.update(kwargs)

class WoofScheme(ColorScheme):
	def __init__(self, **kwargs):

		self.dolphin = "#665984"
		self.cold_turkey = "#C9ACAA"
		self.thunder = "#37292F"

		self.san_juan = "#374D7A"
		self.wedgewood = "#466E98"
		self.casper = "#AFBAD0"
		self.tuna = "#33333E"

		self.jungle_mist = "#C1D2DD"
		self.shadow = "#8A684F"
		self.abbey = "#494A4B"
		self.dolphin_2 = "#6A687B"

		self.black_pearl = "#041D2E"
		self.cadet_blue = "#A9A8C1"
		self.cornflower_blue = "#62A0E8"
		self.mariner = "#2E72BE"

		self.purple = self.dolphin
		self.butter = self.cold_turkey
		self.brown = self.thunder
		self.gray = self.cadet_blue
		self.light_gray = self.casper
		
		self.bg = self.black_pearl
		self.fg = self.casper
		self.current_screen_tab = self.gray
		self.group_name = "#ffffff"
		self.tab_line = self.bg
		self.power1 = self.cornflower_blue
		self.power2 = self.mariner

		self.active = "#ECE4F4"
		self.inactive = "#DFDFDFDF"

		self.window_name = self.active


		
		
		

		

		

		