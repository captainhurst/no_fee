#!/usr/bin/env python
# encoding: utf-8
"""
utils.py

Created by Ryan Hurst on 2013-08-17.
Copyright (c) 2013 Untamed Enterprises LLC. All rights reserved.

from django.core.management.base import BaseCommand, CommandError, NoArgsCommand
import json
from django.template.defaultfilters import slugify
from models import PageModel, PageMeta, PageViewCount, PageContent, Categories


class Command(NoArgsCommand):
	def pop_form(self, **options):
		initial_data = '/Users/captainhurst/scrapy/mesaDentist/yp-output-language-fixed.json'
		
		json_data = open(initial_data, 'r')   
		data = json.load(json_data)
		
		for d in data:
			title_tag = "Mesa Arizona Dental Office | " + str(d.name) 
			slug = slugify(d.name)
			page = PageModel(title_tag=title_tag,descriptive_url=slug )
		    page.save()
			
			md1 = str(d.name) + " " + str(d.dental_services) + " " + str(d.practice_type)
			meta_description = (md1[:200] + '..') if len(md1) > 200 else md1
			keywords = "Mesa Arizona Dentist, Mesa AZ, " + str(d.name) + " " + str(d.dental_services) + " " + str(d.practice_type)
			page_meta = PageMeta(page=page,metaDescription=meta_description, metaKeywords=keywords)
			page_meta.save()
			
			phone_number = str(d.phone_number)
			website = str(d.website)
			name = str(d.name)
			billing = str(d.payment)
			office_hours = str(d.office_hours)
			practice_type = str(d.practice_type)
			address = str(d.address)
			dental_services = str(d.dental_services)
			extra_info = str(d.extra_info)
			
			page_content = PageContent(page=page, phone_number=phone_number,website=website,name=name,billing=billing,office_hours=office_hours,practice_type=practice_type,address=address,dental_services=dental_services,extra_info=extra_info)
			page_content.save()
"""