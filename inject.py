import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    '<a href="#destinos" class="nav-link">Itinerario</a>': '<a href="#destinos" class="nav-link" data-i18n="nav-itinerary">Itinerario</a>',
    '<a href="#gastronomia" class="nav-link">Experiencia</a>': '<a href="#gastronomia" class="nav-link" data-i18n="nav-experience">Experiencia</a>',
    '<a href="#servicios" class="nav-link">Servicios</a>': '<a href="#servicios" class="nav-link" data-i18n="nav-services">Servicios</a>',
    '<a href="#pilares" class="nav-link">Nosotros</a>': '<a href="#pilares" class="nav-link" data-i18n="nav-about">Nosotros</a>',
    '<button class="btn btn-nav" id="navCta" onclick="openModal()">Solicitar Acceso</button>': '<button class="btn btn-nav" id="navCta" onclick="openModal()" data-i18n="nav-cta">Solicitar Acceso</button>',
    
    '<span class="uppercase-tracking gold-text">Smart Meeting Ryder Golf</span>': '<span class="uppercase-tracking gold-text" data-i18n="hero-pretitle">Smart Meeting Ryder Golf</span>',
    'BUSINESS TRIP<br>': '<span data-i18n="hero-title-1">BUSINESS TRIP</span><br>',
    '<span class="serif-italic gold-text">España 2026</span>': '<span class="serif-italic gold-text" data-i18n="hero-title-2">España 2026</span>',
    '<span class="uppercase-tracking" style="color: oklch(0.80 0 0)">Madrid · Sevilla · Ronda · Málaga</span>': '<span class="uppercase-tracking" style="color: oklch(0.80 0 0)" data-i18n="hero-meta-1">Madrid · Sevilla · Ronda · Málaga</span>',
    '<span class="uppercase-tracking" style="color: oklch(0.80 0 0)">27 Septiembre — 07 Octubre</span>': '<span class="uppercase-tracking" style="color: oklch(0.80 0 0)" data-i18n="hero-meta-2">27 Septiembre — 07 Octubre</span>',
    '<button class="btn btn-solid" id="heroCta" onclick="openModal()" style="padding: var(--s3) var(--s6);">Asegure su Lugar</button>': '<button class="btn btn-solid" id="heroCta" onclick="openModal()" style="padding: var(--s3) var(--s6);" data-i18n="hero-cta">Asegure su Lugar</button>',
    
    '<h2 class="section-title" style="color: white;">Ruta del Viaje</h2>': '<h2 class="section-title" style="color: white;" data-i18n="section-route">Ruta del Viaje</h2>',
    
    '<span class="uppercase-tracking gold-text split-label">Destino 01 — Días 1-4</span>': '<span class="uppercase-tracking gold-text split-label" data-i18n="route-1-label">Destino 01 — Días 1-4</span>',
    '<h2 class="split-title">Madrid: El Inicio</h2>': '<h2 class="split-title" data-i18n="route-1-title">Madrid: El Inicio</h2>',
    '<p class="split-desc">La capital de España nos recibe con una agenda diseñada para el impacto empresarial y la excelencia deportiva.</p>': '<p class="split-desc" data-i18n="route-1-desc">La capital de España nos recibe con una agenda diseñada para el impacto empresarial y la excelencia deportiva.</p>',
    '<span><strong>Ryder Golf Madrid:</strong> 2 jornadas épicas de competición.</span>': '<span data-i18n="route-1-li-1"><strong>Ryder Golf Madrid:</strong> 2 jornadas épicas de competición.</span>',
    '<span><strong>Vinology:</strong> Experiencia privada de cata de autor.</span>': '<span data-i18n="route-1-li-2"><strong>Vinology:</strong> Experiencia privada de cata de autor.</span>',
    '<span><strong>Cena de Gala:</strong> Restaurante emblemático del centro histórico.</span>': '<span data-i18n="route-1-li-3"><strong>Cena de Gala:</strong> Restaurante emblemático del centro histórico.</span>',
    
    '<span class="uppercase-tracking gold-text split-label">Destino 02 — Días 5-7</span>': '<span class="uppercase-tracking gold-text split-label" data-i18n="route-2-label">Destino 02 — Días 5-7</span>',
    '<h2 class="split-title">Sevilla: Patrimonio</h2>': '<h2 class="split-title" data-i18n="route-2-title">Sevilla: Patrimonio</h2>',
    '<p class="split-desc">Relación, tradición y gastronomía en el corazón de Andalucía. Una ciudad que respira historia y facilita conexiones genuinas.</p>': '<p class="split-desc" data-i18n="route-2-desc">Relación, tradición y gastronomía en el corazón de Andalucía. Una ciudad que respira historia y facilita conexiones genuinas.</p>',
    '<span><strong>Estancia de Lujo:</strong> Hotel Colón Gran Meliá.</span>': '<span data-i18n="route-2-li-1"><strong>Estancia de Lujo:</strong> Hotel Colón Gran Meliá.</span>',
    '<span><strong>Golf Amistoso:</strong> Formato relajado y relacional.</span>': '<span data-i18n="route-2-li-2"><strong>Golf Amistoso:</strong> Formato relajado y relacional.</span>',
    '<span><strong>Inmersión:</strong> Visita privada a la Catedral y cata de vinos andaluces.</span>': '<span data-i18n="route-2-li-3"><strong>Inmersión:</strong> Visita privada a la Catedral y cata de vinos andaluces.</span>',
    
    '<span class="uppercase-tracking gold-text split-label">Destino 03 — Día 8</span>': '<span class="uppercase-tracking gold-text split-label" data-i18n="route-3-label">Destino 03 — Día 8</span>',
    '<h2 class="split-title">Ronda: Historia</h2>': '<h2 class="split-title" data-i18n="route-3-title">Ronda: Historia</h2>',
    '<p class="split-desc">Un enclave único cortado por el Tajo de Ronda. El maridaje perfecto entre paisaje majestuoso y el mejor vino andaluz.</p>': '<p class="split-desc" data-i18n="route-3-desc">Un enclave único cortado por el Tajo de Ronda. El maridaje perfecto entre paisaje majestuoso y el mejor vino andaluz.</p>',
    '<span><strong>Bodegas Excelencia:</strong> El maridaje perfecto entre paisaje y cata.</span>': '<span data-i18n="route-3-li-1"><strong>Bodegas Excelencia:</strong> El maridaje perfecto entre paisaje y cata.</span>',
    '<span><strong>Paisajes Históricos:</strong> Recorrido guiado por el patrimonio.</span>': '<span data-i18n="route-3-li-2"><strong>Paisajes Históricos:</strong> Recorrido guiado por el patrimonio.</span>',

    '<span class="uppercase-tracking gold-text split-label">Destino 04 — Días 9-11</span>': '<span class="uppercase-tracking gold-text split-label" data-i18n="route-4-label">Destino 04 — Días 9-11</span>',
    '<h2 class="split-title">Málaga: El Cierre</h2>': '<h2 class="split-title" data-i18n="route-4-title">Málaga: El Cierre</h2>',
    '<p class="split-desc">La Costa del Sol marca el broche de oro. Oportunidades finales de negocio frente al resplandeciente Mar Mediterráneo.</p>': '<p class="split-desc" data-i18n="route-4-desc">La Costa del Sol marca el broche de oro. Oportunidades finales de negocio frente al resplandeciente Mar Mediterráneo.</p>',
    '<span><strong>Smart Meeting Málaga:</strong> Conexiones finales antes del regreso.</span>': '<span data-i18n="route-4-li-1"><strong>Smart Meeting Málaga:</strong> Conexiones finales antes del regreso.</span>',
    '<span><strong>Almuerzo en Gutiérrez Puerto</strong> frente al Mediterráneo.</span>': '<span data-i18n="route-4-li-2"><strong>Almuerzo en Gutiérrez Puerto</strong> frente al Mediterráneo.</span>',
    '<span><strong>Golf opcional</strong> y despedida.</span>': '<span data-i18n="route-4-li-3"><strong>Golf opcional</strong> y despedida.</span>',

    '<h2 class="section-title" style="color: white;">Experiencia Gastronómica</h2>': '<h2 class="section-title" style="color: white;" data-i18n="section-gastro">Experiencia Gastronómica</h2>',
    '<h2>El Sabor del Éxito</h2>': '<h2 data-i18n="gastro-title">El Sabor del Éxito</h2>',
    '<p class="gastro-quote">"En cada copa, el vino despliega su poesía líquida, tintando el tiempo con los matices de la tierra."</p>': '<p class="gastro-quote" data-i18n="gastro-quote">"En cada copa, el vino despliega su poesía líquida, tintando el tiempo con los matices de la tierra."</p>',
    '<span>Almuerzos de negocios en locaciones exclusivas.</span>': '<span data-i18n="gastro-li-1">Almuerzos de negocios en locaciones exclusivas.</span>',
    '<span>Catas privadas en las cunas del Tempranillo y el Jerez.</span>': '<span data-i18n="gastro-li-2">Catas privadas en las cunas del Tempranillo y el Jerez.</span>',
    '<span>Cenas en palacios y restaurantes galardonados.</span>': '<span data-i18n="gastro-li-3">Cenas en palacios y restaurantes galardonados.</span>',

    '<p class="bridge-pretitle">De la alta cocina al cierre de tratos.</p>': '<p class="bridge-pretitle" data-i18n="net-pretitle">De la alta cocina al cierre de tratos.</p>',
    '<h2 class="section-title" style="color: white;">Networking Exclusivo</h2>': '<h2 class="section-title" style="color: white;" data-i18n="section-net">Networking Exclusivo</h2>',
    '<p class="section-subtitle net-subtitle-reveal" style="color: oklch(0.60 0 0);">Red Smart Meeting — Acceda a una plataforma tecnológica integrada donde líderes, inversores y profesionales convergen para generar oportunidades reales.</p>': '<p class="section-subtitle net-subtitle-reveal" style="color: oklch(0.60 0 0);" data-i18n="net-subtitle">Red Smart Meeting — Acceda a una plataforma tecnológica integrada donde líderes, inversores y profesionales convergen para generar oportunidades reales.</p>',
    '<h4>Acceso VIP</h4>': '<h4 data-i18n="net-card-1-title">Acceso VIP</h4>',
    '<p>Acceso a clubes privados exclusivos en las principales capitales.</p>': '<p data-i18n="net-card-1-desc">Acceso a clubes privados exclusivos en las principales capitales.</p>',
    '<h4>Presencia Global</h4>': '<h4 data-i18n="net-card-2-title">Presencia Global</h4>',
    '<p>Presencia en las principales capitales económicas del mundo.</p>': '<p data-i18n="net-card-2-desc">Presencia en las principales capitales económicas del mundo.</p>',
    '<h4>Valores</h4>': '<h4 data-i18n="net-card-3-title">Valores</h4>',
    '<p>Ética, Camaradería e Impacto como pilares fundamentales.</p>': '<p data-i18n="net-card-3-desc">Ética, Camaradería e Impacto como pilares fundamentales.</p>',

    '<h2 class="section-title">Servicios VIP Incluidos</h2>': '<h2 class="section-title" data-i18n="section-services">Servicios VIP Incluidos</h2>',
    '<th>Categoría</th>': '<th data-i18n="th-category">Categoría</th>',
    '<th>Detalles del Servicio</th>': '<th data-i18n="th-details">Detalles del Servicio</th>',
    '<td class="vip-category">Hospedaje</td>': '<td class="vip-category" data-i18n="td-cat-1">Hospedaje</td>',
    '<td>Selección de Hoteles 5* Gran Lujo (Ej. Hotel Colón Sevilla).</td>': '<td data-i18n="td-det-1">Selección de Hoteles 5* Gran Lujo (Ej. Hotel Colón Sevilla).</td>',
    '<td class="vip-category">Transporte</td>': '<td class="vip-category" data-i18n="td-cat-2">Transporte</td>',
    '<td>Traslados privados en vehículos de alta gama y vuelos internos.</td>': '<td data-i18n="td-det-2">Traslados privados en vehículos de alta gama y vuelos internos.</td>',
    '<td class="vip-category">Deporte</td>': '<td class="vip-category" data-i18n="td-cat-3">Deporte</td>',
    '<td>Green fees, buggies y coordinación de Torneo Ryder Golf.</td>': '<td data-i18n="td-det-3">Green fees, buggies y coordinación de Torneo Ryder Golf.</td>',
    '<td class="vip-category">Networking</td>': '<td class="vip-category" data-i18n="td-cat-4">Networking</td>',
    '<td>Acceso y organización de 3 eventos Smart Meeting exclusivos.</td>': '<td data-i18n="td-det-4">Acceso y organización de 3 eventos Smart Meeting exclusivos.</td>',

    '<h2 class="esencia-title">Nuestra Esencia</h2>': '<h2 class="esencia-title" data-i18n="section-about">Nuestra Esencia</h2>',
    '<h3 class="pilar-title-mini">Golf</h3>': '<h3 class="pilar-title-mini" data-i18n="about-card-1-title">Golf</h3>',
    '<p class="pilar-desc-mini">Espíritu Ryder en Madrid, formato relacional en Sevilla y jornadas exclusivas en la Costa del Sol.</p>': '<p class="pilar-desc-mini" data-i18n="about-card-1-desc">Espíritu Ryder en Madrid, formato relacional en Sevilla y jornadas exclusivas en la Costa del Sol.</p>',
    '<h3 class="pilar-title-mini">Negocios</h3>': '<h3 class="pilar-title-mini" data-i18n="about-card-2-title">Negocios</h3>',
    '<p class="pilar-desc-mini">Networking de alto nivel con la Red Internacional Smart Meeting en clubes privados de élite.</p>': '<p class="pilar-desc-mini" data-i18n="about-card-2-desc">Networking de alto nivel con la Red Internacional Smart Meeting en clubes privados de élite.</p>',
    '<h3 class="pilar-title-mini">Enología</h3>': '<h3 class="pilar-title-mini" data-i18n="about-card-3-title">Enología</h3>',
    '<p class="pilar-desc-mini">Ruta sensorial por Vinology y Bodegas Excelencia. El vino como hilo conductor del éxito.</p>': '<p class="pilar-desc-mini" data-i18n="about-card-3-desc">Ruta sensorial por Vinology y Bodegas Excelencia. El vino como hilo conductor del éxito.</p>',
    '<h3 class="pilar-title-mini">Cultura</h3>': '<h3 class="pilar-title-mini" data-i18n="about-card-4-title">Cultura</h3>',
    '<p class="pilar-desc-mini">Inmersión en el patrimonio histórico de Ronda, el arte de Sevilla y la modernidad de Madrid.</p>': '<p class="pilar-desc-mini" data-i18n="about-card-4-desc">Inmersión en el patrimonio histórico de Ronda, el arte de Sevilla y la modernidad de Madrid.</p>',

    '<h2 class="esencia-title">Perfil del Grupo</h2>': '<h2 class="esencia-title" data-i18n="about-profile-title">Perfil del Grupo</h2>',
    '<span class="number-label-lg">Jugadores</span>': '<span class="number-label-lg" data-i18n="about-profile-num-1">Jugadores</span>',
    '<span class="number-label-lg">Acompañantes</span>': '<span class="number-label-lg" data-i18n="about-profile-num-2">Acompañantes</span>',
    '<p class="perfil-urgency">Plazas estrictamente limitadas · Asignación por invitación</p>': '<p class="perfil-urgency" data-i18n="about-profile-urgency">Plazas estrictamente limitadas · Asignación por invitación</p>',
    '<h3>Una Experiencia Integral</h3>': '<h3 data-i18n="about-profile-h3">Una Experiencia Integral</h3>',
    '<p>Diseñado para que cada miembro del grupo encuentre valor absoluto. Mientras unos conquistan el green, otros exploran la riqueza social, empresarial y cultural de España.</p>': '<p data-i18n="about-profile-p">Diseñado para que cada miembro del grupo encuentre valor absoluto. Mientras unos conquistan el green, otros exploran la riqueza social, empresarial y cultural de España.</p>',

    '<span class="uppercase-tracking gold-text">Contacto Exclusivo</span>': '<span class="uppercase-tracking gold-text" data-i18n="cierre-pretitle">Contacto Exclusivo</span>',
    '<h2 class="hero-title" style="color: white; font-size: var(--text-3xl);">¿Listo para Unirse?</h2>': '<h2 class="hero-title" style="color: white; font-size: var(--text-3xl);" data-i18n="cierre-title">¿Listo para Unirse?</h2>',
    '<p class="hero-subtitle">Asegure su lugar en esta travesía irrepetible por la geografía del éxito y el deporte.</p>': '<p class="hero-subtitle" data-i18n="cierre-subtitle">Asegure su lugar en esta travesía irrepetible por la geografía del éxito y el deporte.</p>',
    '<button class="btn btn-solid" id="cierreCta" style="padding: var(--s3) var(--s6);" onclick="openModal()">Contactar a Smart Meeting</button>': '<button class="btn btn-solid" id="cierreCta" style="padding: var(--s3) var(--s6);" onclick="openModal()" data-i18n="cierre-cta">Contactar a Smart Meeting</button>',

    '<div class="footer-copy">&copy; 2026 Smart Meeting. Todos los derechos reservados.</div>': '<div class="footer-copy" data-i18n="footer-copy">&copy; 2026 Smart Meeting. Todos los derechos reservados.</div>',

    '<h3 style="font-size: var(--text-2xl); color: white; margin-bottom: var(--s1);">Solicitud de Acceso</h3>': '<h3 style="font-size: var(--text-2xl); color: white; margin-bottom: var(--s1);" data-i18n="modal-title">Solicitud de Acceso</h3>',
    '<p style="color: oklch(0.60 0 0); font-size: var(--text-sm);">Déjenos sus datos para evaluar su perfil y enviarle la invitación oficial.</p>': '<p style="color: oklch(0.60 0 0); font-size: var(--text-sm);" data-i18n="modal-subtitle">Déjenos sus datos para evaluar su perfil y enviarle la invitación oficial.</p>',
    '<label class="form-label" for="fullName">Nombre Completo</label>': '<label class="form-label" for="fullName" data-i18n="modal-label-1">Nombre Completo</label>',
    'placeholder="Ej. Carlos Mendoza"': 'placeholder="Ej. Carlos Mendoza" data-i18n-placeholder="modal-place-1"',
    '<label class="form-label" for="company">Empresa / Cargo</label>': '<label class="form-label" for="company" data-i18n="modal-label-2">Empresa / Cargo</label>',
    'placeholder="CEO en Empresa X"': 'placeholder="CEO en Empresa X" data-i18n-placeholder="modal-place-2"',
    '<label class="form-label" for="email">Email Profesional</label>': '<label class="form-label" for="email" data-i18n="modal-label-3">Email Profesional</label>',
    'placeholder="carlos@empresa.com"': 'placeholder="carlos@empresa.com" data-i18n-placeholder="modal-place-3"',
    '<button type="submit" class="btn btn-solid form-btn">Solicitar mi Invitación</button>': '<button type="submit" class="btn btn-solid form-btn" data-i18n="modal-btn">Solicitar mi Invitación</button>',
    '<p class="form-urgency">Proceso de selección riguroso. Cupos limitados a 30 plazas.</p>': '<p class="form-urgency" data-i18n="modal-urgency">Proceso de selección riguroso. Cupos limitados a 30 plazas.</p>'
}

for k, v in replacements.items():
    content = content.replace(k, v)

# Also add the translation toggle button in the navbar right before <div class="magnetic-wrap"> for navCta
toggle_html = """
        <!-- Language Switcher -->
        <button id="langToggle" class="lang-toggle">
          <i class="ph ph-translate" style="font-size:1.2rem;"></i>
          <span class="lang-text">EN</span>
        </button>
        <div class="magnetic-wrap">"""

content = content.replace('<div class="magnetic-wrap">\n          <button class="btn btn-nav" id="navCta"', toggle_html + '\n          <button class="btn btn-nav" id="navCta"')

# Add <script src="translations.js"></script> before <script src="main.js"></script>
content = content.replace('<script src="main.js"></script>', '<script src="translations.js"></script>\n  <script src="main.js"></script>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
