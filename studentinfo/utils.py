from io import BytesIO, StringIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa
from weasyprint import HTML
from weasyprint.fonts import FontConfiguration

# Commented as using weasyPrint to generate PDF with Marathi Font
# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html  = template.render(context_dict)
#     result = BytesIO()
#     # pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result,encoding='UTF-8')
#     pdf = pisa.pisaDocument(html, result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None

def render_to_pdf(template_src, context_dict={}):
    response = HttpResponse(content_type="application/pdf")

    template = get_template(template_src)
    html = template.render(context_dict)

    font_config = FontConfiguration()
    HTML(string=html,base_url='/home/sanket/Repos/VK/schoolSystem/').write_pdf(response, font_config=font_config,presentational_hints=True)
    return response