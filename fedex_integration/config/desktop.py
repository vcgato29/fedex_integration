# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "fedex_integration",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("fedex_integration")
		}
	]