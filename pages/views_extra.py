
def sitemap_xml(request):
    from django.http import HttpResponse
    sites = []
    for ind in INDUSTRIES:
        sites.append(f"https://example.com/industries/{ind['slug']}/")
    for bot in BOTS:
        sites.append(f"https://example.com/services/bots/{bot['slug']}/")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += '<url><loc>https://example.com/</loc><priority>1.0</priority></url>\n'
    for site in sites:
        xml += f'<url><loc>{site}</loc><priority>0.8</priority></url>\n'
    xml += '</urlset>'
    return HttpResponse(xml, content_type='application/xml')


def robots_txt(request):
    from django.http import HttpResponse
    txt = "User-agent: *\nAllow: /\nSitemap: https://example.com/sitemap.xml\n"
    return HttpResponse(txt, content_type='text/plain')


def search(request):
    query = request.GET.get('q', '').lower()
    results = {'industries': [], 'bots': [], 'services': []}
    if query:
        for ind in INDUSTRIES:
            if query in ind['name'].lower():
                results['industries'].append(ind)
        for bot in BOTS:
            if query in bot['name'].lower():
                results['bots'].append(bot)
        for svc in SERVICES:
            if query in svc['name'].lower():
                results['services'].append(svc)
    return render(request, 'pages/search.html', {'query': query, 'results': results})
