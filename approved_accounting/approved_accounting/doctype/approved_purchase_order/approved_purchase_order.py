# -*- coding: utf-8 -*-
# Copyright (c) 2019, One Asset Management and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from erpnext.erpnext.buying.doctype.purchase_order.purchase_order import PurchaseOrder

class ApprovedPurchaseOrder(PurchaseOrder):
	def __init__(self, *args, **kwargs):
		super(ApprovedPurchaseOrder, self).__init__(*args, **kwargs)

	def validate(self):
		super(ApprovedPurchaseOrder, self).validate()
