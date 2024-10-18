from web.models import *

def cargar_datos():
    chile = Pais.objects.create(nombre="Chile")

    # Región de Arica y Parinacota (XV)
    arica_parinacota = Region.objects.create(nombre="Región de Arica y Parinacota (XV)", pais=chile)

    provincia_arica = Provincia.objects.create(nombre="Provincia de Arica", region=arica_parinacota)
    Comuna.objects.bulk_create([
        Comuna(nombre="Arica", provincia=provincia_arica),
        Comuna(nombre="Camarones", provincia=provincia_arica)
    ])

    provincia_parinacota = Provincia.objects.create(nombre="Provincia de Parinacota", region=arica_parinacota)
    Comuna.objects.bulk_create([
        Comuna(nombre="Putre", provincia=provincia_parinacota),
        Comuna(nombre="General Lagos", provincia=provincia_parinacota)
    ])

    # Región de Tarapacá (I)
    tarapaca = Region.objects.create(nombre="Región de Tarapacá (I)", pais=chile)

    provincia_iquique = Provincia.objects.create(nombre="Provincia de Iquique", region=tarapaca)
    Comuna.objects.bulk_create([
        Comuna(nombre="Iquique", provincia=provincia_iquique),
        Comuna(nombre="Alto Hospicio", provincia=provincia_iquique)
    ])

    provincia_tamarugal = Provincia.objects.create(nombre="Provincia del Tamarugal", region=tarapaca)
    Comuna.objects.bulk_create([
        Comuna(nombre="Pozo Almonte", provincia=provincia_tamarugal),
        Comuna(nombre="Pica", provincia=provincia_tamarugal),
        Comuna(nombre="Huara", provincia=provincia_tamarugal),
        Comuna(nombre="Camiña", provincia=provincia_tamarugal),
        Comuna(nombre="Colchane", provincia=provincia_tamarugal)
    ])

    # Región de Antofagasta (II)
    antofagasta = Region.objects.create(nombre="Región de Antofagasta (II)", pais=chile)

    provincia_antofagasta = Provincia.objects.create(nombre="Provincia de Antofagasta", region=antofagasta)
    Comuna.objects.bulk_create([
        Comuna(nombre="Antofagasta", provincia=provincia_antofagasta),
        Comuna(nombre="Mejillones", provincia=provincia_antofagasta),
        Comuna(nombre="Sierra Gorda", provincia=provincia_antofagasta),
        Comuna(nombre="Taltal", provincia=provincia_antofagasta)
    ])

    provincia_loa = Provincia.objects.create(nombre="Provincia de El Loa", region=antofagasta)
    Comuna.objects.bulk_create([
        Comuna(nombre="Calama", provincia=provincia_loa),
        Comuna(nombre="Ollagüe", provincia=provincia_loa),
        Comuna(nombre="San Pedro de Atacama", provincia=provincia_loa)
    ])

    provincia_tocopilla = Provincia.objects.create(nombre="Provincia de Tocopilla", region=antofagasta)
    Comuna.objects.bulk_create([
        Comuna(nombre="Tocopilla", provincia=provincia_tocopilla),
        Comuna(nombre="María Elena", provincia=provincia_tocopilla)
    ])

    # Región de Atacama (III)
    atacama = Region.objects.create(nombre="Región de Atacama (III)", pais=chile)

    provincia_copiapo = Provincia.objects.create(nombre="Provincia de Copiapó", region=atacama)
    Comuna.objects.bulk_create([
        Comuna(nombre="Copiapó", provincia=provincia_copiapo),
        Comuna(nombre="Tierra Amarilla", provincia=provincia_copiapo)
    ])

    provincia_chanaral = Provincia.objects.create(nombre="Provincia de Chañaral", region=atacama)
    Comuna.objects.bulk_create([
        Comuna(nombre="Chañaral", provincia=provincia_chanaral),
        Comuna(nombre="Diego de Almagro", provincia=provincia_chanaral)
    ])

    provincia_huasco = Provincia.objects.create(nombre="Provincia de Huasco", region=atacama)
    Comuna.objects.bulk_create([
        Comuna(nombre="Vallenar", provincia=provincia_huasco),
        Comuna(nombre="Freirina", provincia=provincia_huasco),
        Comuna(nombre="Huasco", provincia=provincia_huasco),
        Comuna(nombre="Alto del Carmen", provincia=provincia_huasco)
    ])

    # Región de Coquimbo (IV)
    coquimbo = Region.objects.create(nombre="Región de Coquimbo (IV)", pais=chile)

    provincia_elqui = Provincia.objects.create(nombre="Provincia de Elqui", region=coquimbo)
    Comuna.objects.bulk_create([
        Comuna(nombre="La Serena", provincia=provincia_elqui),
        Comuna(nombre="Coquimbo", provincia=provincia_elqui),
        Comuna(nombre="La Higuera", provincia=provincia_elqui),
        Comuna(nombre="Vicuña", provincia=provincia_elqui),
        Comuna(nombre="Paihuano", provincia=provincia_elqui),
        Comuna(nombre="Andacollo", provincia=provincia_elqui)
    ])

    provincia_limari = Provincia.objects.create(nombre="Provincia de Limarí", region=coquimbo)
    Comuna.objects.bulk_create([
        Comuna(nombre="Ovalle", provincia=provincia_limari),
        Comuna(nombre="Monte Patria", provincia=provincia_limari),
        Comuna(nombre="Punitaqui", provincia=provincia_limari),
        Comuna(nombre="Río Hurtado", provincia=provincia_limari),
        Comuna(nombre="Combarbalá", provincia=provincia_limari)
    ])

    provincia_choapa = Provincia.objects.create(nombre="Provincia de Choapa", region=coquimbo)
    Comuna.objects.bulk_create([
        Comuna(nombre="Illapel", provincia=provincia_choapa),
        Comuna(nombre="Salamanca", provincia=provincia_choapa),
        Comuna(nombre="Los Vilos", provincia=provincia_choapa),
        Comuna(nombre="Canela", provincia=provincia_choapa)
    ])

    # Región de Valparaíso (V)
    valparaiso = Region.objects.create(nombre="Región de Valparaíso (V)", pais=chile)

    provincia_valparaiso = Provincia.objects.create(nombre="Provincia de Valparaíso", region=valparaiso)
    Comuna.objects.bulk_create([
        Comuna(nombre="Valparaíso", provincia=provincia_valparaiso),
        Comuna(nombre="Viña del Mar", provincia=provincia_valparaiso),
        Comuna(nombre="Concón", provincia=provincia_valparaiso),
        Comuna(nombre="Quintero", provincia=provincia_valparaiso),
        Comuna(nombre="Puchuncaví", provincia=provincia_valparaiso)
    ])

    provincia_marga_marga = Provincia.objects.create(nombre="Provincia de Marga Marga", region=valparaiso)
    Comuna.objects.bulk_create([
        Comuna(nombre="Quilpué", provincia=provincia_marga_marga),
        Comuna(nombre="Villa Alemana", provincia=provincia_marga_marga),
        Comuna(nombre="Limache", provincia=provincia_marga_marga),
        Comuna(nombre="Olmué", provincia=provincia_marga_marga)
    ])

    provincia_quillota = Provincia.objects.create(nombre="Provincia de Quillota", region=valparaiso)
    Comuna.objects.bulk_create([
        Comuna(nombre="Quillota", provincia=provincia_quillota),
        Comuna(nombre="La Cruz", provincia=provincia_quillota),
        Comuna(nombre="La Calera", provincia=provincia_quillota),
        Comuna(nombre="Nogales", provincia=provincia_quillota),
        Comuna(nombre="Hijuelas", provincia=provincia_quillota)
    ])

    provincia_san_antonio = Provincia.objects.create(nombre="Provincia de San Antonio", region=valparaiso)
    Comuna.objects.bulk_create([
        Comuna(nombre="San Antonio", provincia=provincia_san_antonio),
        Comuna(nombre="Cartagena", provincia=provincia_san_antonio),
        Comuna(nombre="El Quisco", provincia=provincia_san_antonio),
        Comuna(nombre="El Tabo", provincia=provincia_san_antonio),
        Comuna(nombre="Algarrobo", provincia=provincia_san_antonio)
    ])

    provincia_san_felipe = Provincia.objects.create(nombre="Provincia de San Felipe de Aconcagua", region=valparaiso)
    Comuna.objects.bulk_create([
        Comuna(nombre="San Felipe", provincia=provincia_san_felipe),
        Comuna(nombre="Putaendo", provincia=provincia_san_felipe),
        Comuna(nombre="Santa María", provincia=provincia_san_felipe),
        Comuna(nombre="Catemu", provincia=provincia_san_felipe),
        Comuna(nombre="Llaillay", provincia=provincia_san_felipe),
        Comuna(nombre="Panquehue", provincia=provincia_san_felipe)
    ])

    provincia_los_andes = Provincia.objects.create(nombre="Provincia de Los Andes", region=valparaiso)
    Comuna.objects.bulk_create([
        Comuna(nombre="Los Andes", provincia=provincia_los_andes),
        Comuna(nombre="San Esteban", provincia=provincia_los_andes),
        Comuna(nombre="Calle Larga", provincia=provincia_los_andes),
        Comuna(nombre="Rinconada", provincia=provincia_los_andes)
    ])

    provincia_petorca = Provincia.objects.create(nombre="Provincia de Petorca", region=valparaiso)
    Comuna.objects.bulk_create([
        Comuna(nombre="La Ligua", provincia=provincia_petorca),
        Comuna(nombre="Cabildo", provincia=provincia_petorca),
        Comuna(nombre="Papudo", provincia=provincia_petorca),
        Comuna(nombre="Zapallar", provincia=provincia_petorca),
        Comuna(nombre="Petorca", provincia=provincia_petorca)
    ])

    provincia_isla_pascua = Provincia.objects.create(nombre="Provincia de Isla de Pascua", region=valparaiso)
    Comuna.objects.create(nombre="Isla de Pascua (Rapa Nui)", provincia=provincia_isla_pascua)

    # Región Metropolitana de Santiago (RM)
    region_metropolitana = Region.objects.create(nombre="Región Metropolitana de Santiago (RM)", pais=chile)

    provincia_santiago = Provincia.objects.create(nombre="Provincia de Santiago", region=region_metropolitana)
    Comuna.objects.bulk_create([
        Comuna(nombre="Santiago", provincia=provincia_santiago),
        Comuna(nombre="Providencia", provincia=provincia_santiago),
        Comuna(nombre="Ñuñoa", provincia=provincia_santiago),
        Comuna(nombre="La Reina", provincia=provincia_santiago),
        Comuna(nombre="Las Condes", provincia=provincia_santiago),
        Comuna(nombre="Vitacura", provincia=provincia_santiago),
        Comuna(nombre="Lo Barnechea", provincia=provincia_santiago),
        Comuna(nombre="Recoleta", provincia=provincia_santiago),
        Comuna(nombre="Independencia", provincia=provincia_santiago),
        Comuna(nombre="Quinta Normal", provincia=provincia_santiago),
        Comuna(nombre="Renca", provincia=provincia_santiago),
        Comuna(nombre="Conchalí", provincia=provincia_santiago),
        Comuna(nombre="Huechuraba", provincia=provincia_santiago),
        Comuna(nombre="Cerro Navia", provincia=provincia_santiago),
        Comuna(nombre="Lo Prado", provincia=provincia_santiago),
        Comuna(nombre="Estación Central", provincia=provincia_santiago),
        Comuna(nombre="Maipú", provincia=provincia_santiago),
        Comuna(nombre="Pudahuel", provincia=provincia_santiago),
        Comuna(nombre="Cerrillos", provincia=provincia_santiago),
        Comuna(nombre="Pedro Aguirre Cerda", provincia=provincia_santiago),
        Comuna(nombre="San Miguel", provincia=provincia_santiago),
        Comuna(nombre="San Joaquín", provincia=provincia_santiago),
        Comuna(nombre="La Cisterna", provincia=provincia_santiago),
        Comuna(nombre="El Bosque", provincia=provincia_santiago),
        Comuna(nombre="San Ramón", provincia=provincia_santiago),
        Comuna(nombre="La Granja", provincia=provincia_santiago),
        Comuna(nombre="La Florida", provincia=provincia_santiago),
        Comuna(nombre="Peñalolén", provincia=provincia_santiago),
        Comuna(nombre="Macul", provincia=provincia_santiago)
    ])

    provincia_chacabuco = Provincia.objects.create(nombre="Provincia de Chacabuco", region=region_metropolitana)
    Comuna.objects.bulk_create([
        Comuna(nombre="Colina", provincia=provincia_chacabuco),
        Comuna(nombre="Lampa", provincia=provincia_chacabuco),
        Comuna(nombre="Tiltil", provincia=provincia_chacabuco)
    ])

    provincia_cordillera = Provincia.objects.create(nombre="Provincia de Cordillera", region=region_metropolitana)
    Comuna.objects.bulk_create([
        Comuna(nombre="Puente Alto", provincia=provincia_cordillera),
        Comuna(nombre="Pirque", provincia=provincia_cordillera),
        Comuna(nombre="San José de Maipo", provincia=provincia_cordillera)
    ])

    provincia_maipo = Provincia.objects.create(nombre="Provincia de Maipo", region=region_metropolitana)
    Comuna.objects.bulk_create([
        Comuna(nombre="San Bernardo", provincia=provincia_maipo),
        Comuna(nombre="Buin", provincia=provincia_maipo),
        Comuna(nombre="Paine", provincia=provincia_maipo),
        Comuna(nombre="Calera de Tango", provincia=provincia_maipo)
    ])

    provincia_melipilla = Provincia.objects.create(nombre="Provincia de Melipilla", region=region_metropolitana)
    Comuna.objects.bulk_create([
        Comuna(nombre="Melipilla", provincia=provincia_melipilla),
        Comuna(nombre="Alhúe", provincia=provincia_melipilla),
        Comuna(nombre="Curacaví", provincia=provincia_melipilla),
        Comuna(nombre="María Pinto", provincia=provincia_melipilla),
        Comuna(nombre="San Pedro", provincia=provincia_melipilla),
    ])

    provincia_talagante = Provincia.objects.create(nombre="Provincia de Talagante", region=region_metropolitana)
    Comuna.objects.bulk_create([
        Comuna(nombre="Talagante", provincia=provincia_talagante),
        Comuna(nombre="Peñaflor", provincia=provincia_talagante),
        Comuna(nombre="Isla de Maipo", provincia=provincia_talagante),
        Comuna(nombre="El Monte", provincia=provincia_talagante),
        Comuna(nombre="Padre Hurtado", provincia=provincia_talagante)
    ])

    # Región del Libertador General Bernardo O'Higgins (VI)
    libertador_general_bernardo_ohiggins = Region.objects.create(nombre="Región del Libertador General Bernardo O'Higgins (VI)", pais=chile)

    provincia_cachapoal = Provincia.objects.create(nombre="Provincia de Cachapoal", region=libertador_general_bernardo_ohiggins)
    Comuna.objects.bulk_create([
        Comuna(nombre="Rancagua", provincia=provincia_cachapoal),
        Comuna(nombre="Machalí", provincia=provincia_cachapoal),
        Comuna(nombre="Graneros", provincia=provincia_cachapoal),
        Comuna(nombre="Codegua", provincia=provincia_cachapoal),
        Comuna(nombre="Requínoa", provincia=provincia_cachapoal),
        Comuna(nombre="Rengo", provincia=provincia_cachapoal),
        Comuna(nombre="Olivar", provincia=provincia_cachapoal),
        Comuna(nombre="Doñihue", provincia=provincia_cachapoal),
        Comuna(nombre="Coltauco", provincia=provincia_cachapoal),
        Comuna(nombre="Coinco", provincia=provincia_cachapoal),
        Comuna(nombre="Quinta de Tiltoco", provincia=provincia_cachapoal),
        Comuna(nombre="San Vicente de Tagua Tagua", provincia=provincia_cachapoal),
        Comuna(nombre="Malloa", provincia=provincia_cachapoal)
    ])

    provincia_colchagua= Provincia.objects.create(nombre="Provincia de Colchagua", region=libertador_general_bernardo_ohiggins)
    Comuna.objects.bulk_create([
        Comuna(nombre="San Fernando", provincia=provincia_colchagua),
        Comuna(nombre="Santa Cruz", provincia=provincia_colchagua),
        Comuna(nombre="Chimbarongo", provincia=provincia_colchagua),
        Comuna(nombre="Nancagua", provincia=provincia_colchagua),
        Comuna(nombre="Palmilla", provincia=provincia_colchagua),
        Comuna(nombre="Peralillo", provincia=provincia_colchagua),
        Comuna(nombre="Placilla", provincia=provincia_colchagua),
        Comuna(nombre="Pumanque", provincia=provincia_colchagua),
        Comuna(nombre="Lolol", provincia=provincia_colchagua),
        Comuna(nombre="Chépica", provincia=provincia_colchagua),
    ])

    provincia_cardenal_caro = Provincia.objects.create(nombre="Provincia de Cardenal Caro", region=libertador_general_bernardo_ohiggins)
    Comuna.objects.bulk_create([
        Comuna(nombre="Pichilemu", provincia=provincia_cardenal_caro),
        Comuna(nombre="Marchigüe", provincia=provincia_cardenal_caro),
        Comuna(nombre="Litueche", provincia=provincia_cardenal_caro),
        Comuna(nombre="La Estrella", provincia=provincia_cardenal_caro),
        Comuna(nombre="Paredones", provincia=provincia_cardenal_caro),
        Comuna(nombre="Navidad", provincia=provincia_cardenal_caro)
    ])
    

    # Región del Maule (VII)
    maule = Region.objects.create(nombre="Región del Maule (VII)", pais=chile)

    provincia_talca = Provincia.objects.create(nombre="Provincia de Talca", region=maule)
    Comuna.objects.bulk_create([
        Comuna(nombre="Talca", provincia=provincia_talca),
        Comuna(nombre="San Clemente", provincia=provincia_talca),
        Comuna(nombre="Pelarco", provincia=provincia_talca),
        Comuna(nombre="Pencahue", provincia=provincia_talca),
        Comuna(nombre="Maule", provincia=provincia_talca),
        Comuna(nombre="Curepto", provincia=provincia_talca),
        Comuna(nombre="Constitución", provincia=provincia_talca),
        Comuna(nombre="Empedrado", provincia=provincia_talca),
        Comuna(nombre="Río Claro", provincia=provincia_talca)
    ])

    provincia_curico = Provincia.objects.create(nombre="Provincia de Curicó", region=maule)
    Comuna.objects.bulk_create([
        Comuna(nombre="Curicó", provincia=provincia_curico),
        Comuna(nombre="Hualañé", provincia=provincia_curico),
        Comuna(nombre="Licantén", provincia=provincia_curico),
        Comuna(nombre="Molina", provincia=provincia_curico),
        Comuna(nombre="Rauco", provincia=provincia_curico),
        Comuna(nombre="Romeral", provincia=provincia_curico),
        Comuna(nombre="Sagrada Familia", provincia=provincia_curico),
        Comuna(nombre="Vichuquén", provincia=provincia_curico)
    ])

    provincia_linares = Provincia.objects.create(nombre="Provincia de Linares", region=maule)
    Comuna.objects.bulk_create([
        Comuna(nombre="Linares", provincia=provincia_linares),
        Comuna(nombre="Longaví", provincia=provincia_linares),
        Comuna(nombre="Colbún", provincia=provincia_linares),
        Comuna(nombre="San Javier", provincia=provincia_linares),
        Comuna(nombre="Villa Alegre", provincia=provincia_linares),
        Comuna(nombre="Yerbas Buenas", provincia=provincia_linares),
        Comuna(nombre="Parral", provincia=provincia_linares)
    ])

    provincia_cauquenes = Provincia.objects.create(nombre="Provincia de Cauquenes", region=maule)
    Comuna.objects.bulk_create([
        Comuna(nombre="Cauquenes", provincia=provincia_cauquenes),
        Comuna(nombre="Chanco", provincia=provincia_cauquenes),
        Comuna(nombre="Pelluhue", provincia=provincia_cauquenes)
    ])

    # Región de Ñuble (XVI)
    ñuble = Region.objects.create(nombre="Región de Ñuble (XVI)", pais=chile)

    provincia_diguillin = Provincia.objects.create(nombre="Provincia de Diguillín", region=ñuble)
    Comuna.objects.bulk_create([
        Comuna(nombre="Chillán", provincia=provincia_diguillin),
        Comuna(nombre="Chillán Viejo", provincia=provincia_diguillin),
        Comuna(nombre="El Carmen", provincia=provincia_diguillin),
        Comuna(nombre="Pemuco", provincia=provincia_diguillin),
        Comuna(nombre="Pinto", provincia=provincia_diguillin),
        Comuna(nombre="San Ignacio", provincia=provincia_diguillin),
        Comuna(nombre="Yungay", provincia=provincia_diguillin)
    ])

    provincia_itata = Provincia.objects.create(nombre="Provincia de Itata", region=ñuble)
    Comuna.objects.bulk_create([
        Comuna(nombre="Cobquecura", provincia=provincia_itata),
        Comuna(nombre="Coelemu", provincia=provincia_itata),
        Comuna(nombre="Ninhue", provincia=provincia_itata),
        Comuna(nombre="Portezuelo", provincia=provincia_itata),
        Comuna(nombre="Quirihue", provincia=provincia_itata),
        Comuna(nombre="Ránquil", provincia=provincia_itata),
        Comuna(nombre="Trehuaco", provincia=provincia_itata)
    ])

    provincia_punilla = Provincia.objects.create(nombre="Provincia de Punilla", region=ñuble)
    Comuna.objects.bulk_create([
        Comuna(nombre="San Carlos", provincia=provincia_punilla),
        Comuna(nombre="Coihueco", provincia=provincia_punilla),
        Comuna(nombre="Ñiquén", provincia=provincia_punilla),
        Comuna(nombre="San Fabián", provincia=provincia_punilla)
    ])

    # Región del Biobío (VIII))
    biobio = Region.objects.create(nombre="Región del Biobío (VIII)", pais=chile)

    provincia_concepcion = Provincia.objects.create(nombre="Provincia de Concepción", region=biobio)
    Comuna.objects.bulk_create([
        Comuna(nombre="Concepción", provincia=provincia_concepcion),
        Comuna(nombre="Talcahuano", provincia=provincia_concepcion),
        Comuna(nombre="Hualpén", provincia=provincia_concepcion),
        Comuna(nombre="San Pedro de la Paz", provincia=provincia_concepcion),
        Comuna(nombre="Chiguayante", provincia=provincia_concepcion),
        Comuna(nombre="Penco", provincia=provincia_concepcion),
        Comuna(nombre="Tomé", provincia=provincia_concepcion),
        Comuna(nombre="Coronel", provincia=provincia_concepcion),
        Comuna(nombre="Lota", provincia=provincia_concepcion),
        Comuna(nombre="Hualqui", provincia=provincia_concepcion),
        Comuna(nombre="Santa Juana", provincia=provincia_concepcion),
        Comuna(nombre="Florida", provincia=provincia_concepcion)
    ])

    provincia_arauco = Provincia.objects.create(nombre="Provincia de Arauco", region=biobio)
    Comuna.objects.bulk_create([
        Comuna(nombre="Arauco", provincia=provincia_arauco),
        Comuna(nombre="Coranilahue", provincia=provincia_arauco),
        Comuna(nombre="Lebu", provincia=provincia_arauco),
        Comuna(nombre="Los Álamos", provincia=provincia_arauco),
        Comuna(nombre="Cañete", provincia=provincia_arauco),
        Comuna(nombre="Contulmo", provincia=provincia_arauco),
        Comuna(nombre="Tirúa", provincia=provincia_arauco)
    ])

    provincia_biobio = Provincia.objects.create(nombre="Provincia de Biobío", region=biobio)
    Comuna.objects.bulk_create([
        Comuna(nombre="Los Ángeles", provincia=provincia_biobio),
        Comuna(nombre="Laja", provincia=provincia_biobio),
        Comuna(nombre="Mulchén", provincia=provincia_biobio),
        Comuna(nombre="Nacimiento", provincia=provincia_biobio),
        Comuna(nombre="Negrete", provincia=provincia_biobio),
        Comuna(nombre="San Rosendo", provincia=provincia_biobio),
        Comuna(nombre="Santa Bárbara", provincia=provincia_biobio),
        Comuna(nombre="Quilaco", provincia=provincia_biobio),
        Comuna(nombre="Quileco", provincia=provincia_biobio),
        Comuna(nombre="Yumbel", provincia=provincia_biobio),
        Comuna(nombre="Cabrero", provincia=provincia_biobio),
        Comuna(nombre="Tucapel", provincia=provincia_biobio),
        Comuna(nombre="Alto Biobío", provincia=provincia_biobio)
    ])

    # Región de La Araucanía (IX)
    araucania = Region.objects.create(nombre="Región de La Araucanía (IX)", pais=chile)

    provincia_cautin = Provincia.objects.create(nombre="Provincia de Cautín", region=araucania)
    Comuna.objects.bulk_create([
        Comuna(nombre="Temuco", provincia=provincia_cautin),
        Comuna(nombre="Padre Las Casas", provincia=provincia_cautin),
        Comuna(nombre="Vilcún", provincia=provincia_cautin),
        Comuna(nombre="Lautaro", provincia=provincia_cautin),
        Comuna(nombre="Perquenco", provincia=provincia_cautin),
        Comuna(nombre="Galvarino", provincia=provincia_cautin),
        Comuna(nombre="Nueva Imperial", provincia=provincia_cautin),
        Comuna(nombre="Cholchol", provincia=provincia_cautin),
        Comuna(nombre="Saavedra", provincia=provincia_cautin),
        Comuna(nombre="Freire", provincia=provincia_cautin),
        Comuna(nombre="Pitrufquén", provincia=provincia_cautin),
        Comuna(nombre="Teodoro Schmidt", provincia=provincia_cautin),
        Comuna(nombre="Toltén", provincia=provincia_cautin),
        Comuna(nombre="Loncoche", provincia=provincia_cautin),
        Comuna(nombre="Gorbea", provincia=provincia_cautin),
        Comuna(nombre="Cunco", provincia=provincia_cautin),
        Comuna(nombre="Melipeuco", provincia=provincia_cautin)
    ])

    provincia_malleco = Provincia.objects.create(nombre="Provincia de Malleco", region=araucania)
    Comuna.objects.bulk_create([
        Comuna(nombre="Angol", provincia=provincia_malleco),
        Comuna(nombre="Renaico", provincia=provincia_malleco),
        Comuna(nombre="Collipulli", provincia=provincia_malleco),
        Comuna(nombre="Ercilla", provincia=provincia_malleco),
        Comuna(nombre="Lonquimay", provincia=provincia_malleco),
        Comuna(nombre="Curicautín", provincia=provincia_malleco),
        Comuna(nombre="Victoria", provincia=provincia_malleco),
        Comuna(nombre="Traiguén", provincia=provincia_malleco),
        Comuna(nombre="Lumaco", provincia=provincia_malleco),
        Comuna(nombre="Los Sauces", provincia=provincia_malleco),
        Comuna(nombre="Purén", provincia=provincia_malleco)
    ])

    # Región de Los Ríos (XIV)
    rios = Region.objects.create(nombre="Región de Los Ríos (XIV)", pais=chile)

    provincia_valdivia = Provincia.objects.create(nombre="Provincia de Valdivia", region=rios)
    Comuna.objects.bulk_create([
        Comuna(nombre="Valdivia", provincia=provincia_valdivia),
        Comuna(nombre="Corral", provincia=provincia_valdivia),
        Comuna(nombre="Lanco", provincia=provincia_valdivia),
        Comuna(nombre="Máfil", provincia=provincia_valdivia),
        Comuna(nombre="Mariquina", provincia=provincia_valdivia),
        Comuna(nombre="Panguipulli", provincia=provincia_valdivia),
        Comuna(nombre="Los Lagos", provincia=provincia_valdivia),
        Comuna(nombre="Paillaco", provincia=provincia_valdivia)
    ])

    provincia_ranco = Provincia.objects.create(nombre="Provincia del Ranco", region=rios)
    Comuna.objects.bulk_create([
        Comuna(nombre="La Unión", provincia=provincia_ranco),
        Comuna(nombre="Futrono", provincia=provincia_ranco),
        Comuna(nombre="Lago Ranco", provincia=provincia_ranco),
        Comuna(nombre="Río Bueno", provincia=provincia_ranco)
    ])

    # Región de Los Lagos (X)
    lagos = Region.objects.create(nombre="Región de Los Lagos (X)", pais=chile)

    provincia_llanquihue = Provincia.objects.create(nombre="Provincia de Llanquihue", region=lagos)
    Comuna.objects.bulk_create([
        Comuna(nombre="Puerto Montt", provincia=provincia_llanquihue),
        Comuna(nombre="Puerto Varas", provincia=provincia_llanquihue),
        Comuna(nombre="Llanquihue", provincia=provincia_llanquihue),
        Comuna(nombre="Frutillar", provincia=provincia_llanquihue),
        Comuna(nombre="Los Muermos", provincia=provincia_llanquihue),
        Comuna(nombre="Fresia", provincia=provincia_llanquihue),
        Comuna(nombre="Maullín", provincia=provincia_llanquihue),
        Comuna(nombre="Calbuco", provincia=provincia_llanquihue)
    ])

    provincia_chiloe = Provincia.objects.create(nombre="Provincia de Chiloé", region=lagos)
    Comuna.objects.bulk_create([
        Comuna(nombre="Castro", provincia=provincia_chiloe),
        Comuna(nombre="Ancud", provincia=provincia_chiloe),
        Comuna(nombre="Chonchi", provincia=provincia_chiloe),
        Comuna(nombre="Dalcahue", provincia=provincia_chiloe),
        Comuna(nombre="Curaco de Vélez", provincia=provincia_chiloe),
        Comuna(nombre="Queilén", provincia=provincia_chiloe),
        Comuna(nombre="Quellón", provincia=provincia_chiloe),
        Comuna(nombre="Quemchi", provincia=provincia_chiloe),
        Comuna(nombre="Puqueldón", provincia=provincia_chiloe)
    ])

    provincia_osorno = Provincia.objects.create(nombre="Provincia de Osorno", region=lagos)
    Comuna.objects.bulk_create([
        Comuna(nombre="Osorno", provincia=provincia_osorno),
        Comuna(nombre="San Pablo", provincia=provincia_osorno),
        Comuna(nombre="San Juan de la Costa", provincia=provincia_osorno),
        Comuna(nombre="Purranque", provincia=provincia_osorno),
        Comuna(nombre="Río Negro", provincia=provincia_osorno),
        Comuna(nombre="Puerto Octay", provincia=provincia_osorno)
    ])

    provincia_palena = Provincia.objects.create(nombre="Provincia de Palena", region=lagos)
    Comuna.objects.bulk_create([
        Comuna(nombre="Chaitén", provincia=provincia_palena),
        Comuna(nombre="Futaleufú", provincia=provincia_palena),
        Comuna(nombre="Palena", provincia=provincia_palena),
        Comuna(nombre="Hualaihúe", provincia=provincia_palena)
    ])

    # Región de Aysén del General Carlos Ibáñez del Campo (XI)
    aysen = Region.objects.create(nombre="Región de Aysén del General Carlos Ibáñez del Campo (XI)", pais=chile)

    provincia_coyhaique = Provincia.objects.create(nombre="Provincia de Coyhaique", region=aysen)
    Comuna.objects.bulk_create([
        Comuna(nombre="Coyhaique", provincia=provincia_coyhaique),
        Comuna(nombre="Lago Verde", provincia=provincia_coyhaique)
    ])

    provincia_aysen = Provincia.objects.create(nombre="Provincia de Aysén", region=aysen)
    Comuna.objects.bulk_create([
        Comuna(nombre="Aysén", provincia=provincia_aysen),
        Comuna(nombre="Cisnes", provincia=provincia_aysen),
        Comuna(nombre="Guaitecas", provincia=provincia_aysen)
    ])

    provincia_general_carrera = Provincia.objects.create(nombre="Provincia de General Carrera", region=aysen)
    Comuna.objects.bulk_create([
        Comuna(nombre="Chile Chico", provincia=provincia_general_carrera),
        Comuna(nombre="Río Ibáñez", provincia=provincia_general_carrera)
    ])

    provincia_capitan_prat = Provincia.objects.create(nombre="Provincia de Capitán Prat", region=aysen)
    Comuna.objects.bulk_create([
        Comuna(nombre="Cochrane", provincia=provincia_capitan_prat),
        Comuna(nombre="Tortel", provincia=provincia_capitan_prat),
        Comuna(nombre="O'Higgiins", provincia=provincia_capitan_prat)
    ])

    # Región de Magallanes y de la Antártica Chilena (XII)
    magallanes_antartica_chilena = Region.objects.create(nombre="Región de Magallanes y de la Antártica Chilena (XII)", pais=chile)

    provincia_magallanes = Provincia.objects.create(nombre="Provincia de Magallanes", region=magallanes_antartica_chilena)
    Comuna.objects.bulk_create([
        Comuna(nombre="Punta Arenas", provincia=provincia_magallanes),
        Comuna(nombre="Laguna Blanca", provincia=provincia_magallanes),
        Comuna(nombre="Rio Verde", provincia=provincia_magallanes),
        Comuna(nombre="San Gregorio", provincia=provincia_magallanes)
    ])

    provincia_tierra_fuego = Provincia.objects.create(nombre="Provincia de Tierra del Fuego", region=magallanes_antartica_chilena)
    Comuna.objects.bulk_create([
        Comuna(nombre="Porvenir", provincia=provincia_tierra_fuego),
        Comuna(nombre="Primavera", provincia=provincia_tierra_fuego),
        Comuna(nombre="Timaukel", provincia=provincia_tierra_fuego)
    ])

    provincia_utlima_esperanza = Provincia.objects.create(nombre="Provincia de Última Esperanza", region=magallanes_antartica_chilena)
    Comuna.objects.bulk_create([
        Comuna(nombre="Puerto Natales", provincia=provincia_utlima_esperanza),
        Comuna(nombre="Torres del Paine", provincia=provincia_utlima_esperanza)
    ])

    provincia_antartica_chilena = Provincia.objects.create(nombre="Provincia de la Antártica Chilena", region=magallanes_antartica_chilena)
    Comuna.objects.bulk_create([
        Comuna(nombre="Cabo de Hornos", provincia=provincia_antartica_chilena),
        Comuna(nombre="Antártica", provincia=provincia_antartica_chilena)
    ])


    print("Datos cargados exitosamente")

if __name__ == '__main__':
    cargar_datos()
