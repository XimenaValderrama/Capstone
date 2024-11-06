from web.models import *

def cargar_datos_mascota():
    chile = PaisMascota.objects.create(nombre="Chile")

    # Región de Arica y Parinacota (XV)
    arica_parinacota = RegionMascota.objects.create(nombre="Región de Arica y Parinacota (XV)", pais=chile)

    provincia_arica = ProvinciaMascota.objects.create(nombre="Provincia de Arica", region=arica_parinacota)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Arica", provincia=provincia_arica),
        ComunaMascota(nombre="Camarones", provincia=provincia_arica)
    ])

    provincia_parinacota = ProvinciaMascota.objects.create(nombre="Provincia de Parinacota", region=arica_parinacota)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Putre", provincia=provincia_parinacota),
        ComunaMascota(nombre="General Lagos", provincia=provincia_parinacota)
    ])

    # Región de Tarapacá (I)
    tarapaca = RegionMascota.objects.create(nombre="Región de Tarapacá (I)", pais=chile)

    provincia_iquique = ProvinciaMascota.objects.create(nombre="Provincia de Iquique", region=tarapaca)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Iquique", provincia=provincia_iquique),
        ComunaMascota(nombre="Alto Hospicio", provincia=provincia_iquique)
    ])

    provincia_tamarugal = ProvinciaMascota.objects.create(nombre="Provincia del Tamarugal", region=tarapaca)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Pozo Almonte", provincia=provincia_tamarugal),
        ComunaMascota(nombre="Pica", provincia=provincia_tamarugal),
        ComunaMascota(nombre="Huara", provincia=provincia_tamarugal),
        ComunaMascota(nombre="Camiña", provincia=provincia_tamarugal),
        ComunaMascota(nombre="Colchane", provincia=provincia_tamarugal)
    ])

    # Región de Antofagasta (II)
    antofagasta = RegionMascota.objects.create(nombre="Región de Antofagasta (II)", pais=chile)

    provincia_antofagasta = ProvinciaMascota.objects.create(nombre="Provincia de Antofagasta", region=antofagasta)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Antofagasta", provincia=provincia_antofagasta),
        ComunaMascota(nombre="Mejillones", provincia=provincia_antofagasta),
        ComunaMascota(nombre="Sierra Gorda", provincia=provincia_antofagasta),
        ComunaMascota(nombre="Taltal", provincia=provincia_antofagasta)
    ])

    provincia_loa = ProvinciaMascota.objects.create(nombre="Provincia de El Loa", region=antofagasta)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Calama", provincia=provincia_loa),
        ComunaMascota(nombre="Ollagüe", provincia=provincia_loa),
        ComunaMascota(nombre="San Pedro de Atacama", provincia=provincia_loa)
    ])

    provincia_tocopilla = ProvinciaMascota.objects.create(nombre="Provincia de Tocopilla", region=antofagasta)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Tocopilla", provincia=provincia_tocopilla),
        ComunaMascota(nombre="María Elena", provincia=provincia_tocopilla)
    ])

    # Región de Atacama (III)
    atacama = RegionMascota.objects.create(nombre="Región de Atacama (III)", pais=chile)

    provincia_copiapo = ProvinciaMascota.objects.create(nombre="Provincia de Copiapó", region=atacama)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Copiapó", provincia=provincia_copiapo),
        ComunaMascota(nombre="Tierra Amarilla", provincia=provincia_copiapo)
    ])

    provincia_chanaral = ProvinciaMascota.objects.create(nombre="Provincia de Chañaral", region=atacama)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Chañaral", provincia=provincia_chanaral),
        ComunaMascota(nombre="Diego de Almagro", provincia=provincia_chanaral)
    ])

    provincia_huasco = ProvinciaMascota.objects.create(nombre="Provincia de Huasco", region=atacama)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Vallenar", provincia=provincia_huasco),
        ComunaMascota(nombre="Freirina", provincia=provincia_huasco),
        ComunaMascota(nombre="Huasco", provincia=provincia_huasco),
        ComunaMascota(nombre="Alto del Carmen", provincia=provincia_huasco)
    ])

    # Región de Coquimbo (IV)
    coquimbo = RegionMascota.objects.create(nombre="Región de Coquimbo (IV)", pais=chile)

    provincia_elqui = ProvinciaMascota.objects.create(nombre="Provincia de Elqui", region=coquimbo)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="La Serena", provincia=provincia_elqui),
        ComunaMascota(nombre="Coquimbo", provincia=provincia_elqui),
        ComunaMascota(nombre="La Higuera", provincia=provincia_elqui),
        ComunaMascota(nombre="Vicuña", provincia=provincia_elqui),
        ComunaMascota(nombre="Paihuano", provincia=provincia_elqui),
        ComunaMascota(nombre="Andacollo", provincia=provincia_elqui)
    ])

    provincia_limari = ProvinciaMascota.objects.create(nombre="Provincia de Limarí", region=coquimbo)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Ovalle", provincia=provincia_limari),
        ComunaMascota(nombre="Monte Patria", provincia=provincia_limari),
        ComunaMascota(nombre="Punitaqui", provincia=provincia_limari),
        ComunaMascota(nombre="Río Hurtado", provincia=provincia_limari),
        ComunaMascota(nombre="Combarbalá", provincia=provincia_limari)
    ])

    provincia_choapa = ProvinciaMascota.objects.create(nombre="Provincia de Choapa", region=coquimbo)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Illapel", provincia=provincia_choapa),
        ComunaMascota(nombre="Salamanca", provincia=provincia_choapa),
        ComunaMascota(nombre="Los Vilos", provincia=provincia_choapa),
        ComunaMascota(nombre="Canela", provincia=provincia_choapa)
    ])

    # Región de Valparaíso (V)
    valparaiso = RegionMascota.objects.create(nombre="Región de Valparaíso (V)", pais=chile)

    provincia_valparaiso = ProvinciaMascota.objects.create(nombre="Provincia de Valparaíso", region=valparaiso)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Valparaíso", provincia=provincia_valparaiso),
        ComunaMascota(nombre="Viña del Mar", provincia=provincia_valparaiso),
        ComunaMascota(nombre="Concón", provincia=provincia_valparaiso),
        ComunaMascota(nombre="Quintero", provincia=provincia_valparaiso),
        ComunaMascota(nombre="Puchuncaví", provincia=provincia_valparaiso)
    ])

    provincia_marga_marga = ProvinciaMascota.objects.create(nombre="Provincia de Marga Marga", region=valparaiso)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Quilpué", provincia=provincia_marga_marga),
        ComunaMascota(nombre="Villa Alemana", provincia=provincia_marga_marga),
        ComunaMascota(nombre="Limache", provincia=provincia_marga_marga),
        ComunaMascota(nombre="Olmué", provincia=provincia_marga_marga)
    ])

    provincia_quillota = ProvinciaMascota.objects.create(nombre="Provincia de Quillota", region=valparaiso)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Quillota", provincia=provincia_quillota),
        ComunaMascota(nombre="La Cruz", provincia=provincia_quillota),
        ComunaMascota(nombre="La Calera", provincia=provincia_quillota),
        ComunaMascota(nombre="Nogales", provincia=provincia_quillota),
        ComunaMascota(nombre="Hijuelas", provincia=provincia_quillota)
    ])

    provincia_san_antonio = ProvinciaMascota.objects.create(nombre="Provincia de San Antonio", region=valparaiso)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="San Antonio", provincia=provincia_san_antonio),
        ComunaMascota(nombre="Cartagena", provincia=provincia_san_antonio),
        ComunaMascota(nombre="El Quisco", provincia=provincia_san_antonio),
        ComunaMascota(nombre="El Tabo", provincia=provincia_san_antonio),
        ComunaMascota(nombre="Algarrobo", provincia=provincia_san_antonio)
    ])

    provincia_san_felipe = ProvinciaMascota.objects.create(nombre="Provincia de San Felipe de Aconcagua", region=valparaiso)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="San Felipe", provincia=provincia_san_felipe),
        ComunaMascota(nombre="Putaendo", provincia=provincia_san_felipe),
        ComunaMascota(nombre="Santa María", provincia=provincia_san_felipe),
        ComunaMascota(nombre="Catemu", provincia=provincia_san_felipe),
        ComunaMascota(nombre="Llaillay", provincia=provincia_san_felipe),
        ComunaMascota(nombre="Panquehue", provincia=provincia_san_felipe)
    ])

    provincia_los_andes = ProvinciaMascota.objects.create(nombre="Provincia de Los Andes", region=valparaiso)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Los Andes", provincia=provincia_los_andes),
        ComunaMascota(nombre="San Esteban", provincia=provincia_los_andes),
        ComunaMascota(nombre="Calle Larga", provincia=provincia_los_andes),
        ComunaMascota(nombre="Rinconada", provincia=provincia_los_andes)
    ])

    provincia_petorca = ProvinciaMascota.objects.create(nombre="Provincia de Petorca", region=valparaiso)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="La Ligua", provincia=provincia_petorca),
        ComunaMascota(nombre="Cabildo", provincia=provincia_petorca),
        ComunaMascota(nombre="Papudo", provincia=provincia_petorca),
        ComunaMascota(nombre="Zapallar", provincia=provincia_petorca),
        ComunaMascota(nombre="Petorca", provincia=provincia_petorca)
    ])

    provincia_isla_pascua = ProvinciaMascota.objects.create(nombre="Provincia de Isla de Pascua", region=valparaiso)
    ComunaMascota.objects.create(nombre="Isla de Pascua (Rapa Nui)", provincia=provincia_isla_pascua)

    # Región Metropolitana de Santiago (RM)
    region_metropolitana = RegionMascota.objects.create(nombre="Región Metropolitana de Santiago (RM)", pais=chile)

    provincia_santiago = ProvinciaMascota.objects.create(nombre="Provincia de Santiago", region=region_metropolitana)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Santiago", provincia=provincia_santiago),
        ComunaMascota(nombre="Providencia", provincia=provincia_santiago),
        ComunaMascota(nombre="Ñuñoa", provincia=provincia_santiago),
        ComunaMascota(nombre="La Reina", provincia=provincia_santiago),
        ComunaMascota(nombre="Las Condes", provincia=provincia_santiago),
        ComunaMascota(nombre="Vitacura", provincia=provincia_santiago),
        ComunaMascota(nombre="Lo Barnechea", provincia=provincia_santiago),
        ComunaMascota(nombre="Recoleta", provincia=provincia_santiago),
        ComunaMascota(nombre="Independencia", provincia=provincia_santiago),
        ComunaMascota(nombre="Quinta Normal", provincia=provincia_santiago),
        ComunaMascota(nombre="Renca", provincia=provincia_santiago),
        ComunaMascota(nombre="Conchalí", provincia=provincia_santiago),
        ComunaMascota(nombre="Huechuraba", provincia=provincia_santiago),
        ComunaMascota(nombre="Cerro Navia", provincia=provincia_santiago),
        ComunaMascota(nombre="Lo Prado", provincia=provincia_santiago),
        ComunaMascota(nombre="Estación Central", provincia=provincia_santiago),
        ComunaMascota(nombre="Maipú", provincia=provincia_santiago),
        ComunaMascota(nombre="Pudahuel", provincia=provincia_santiago),
        ComunaMascota(nombre="Cerrillos", provincia=provincia_santiago),
        ComunaMascota(nombre="Pedro Aguirre Cerda", provincia=provincia_santiago),
        ComunaMascota(nombre="San Miguel", provincia=provincia_santiago),
        ComunaMascota(nombre="San Joaquín", provincia=provincia_santiago),
        ComunaMascota(nombre="La Cisterna", provincia=provincia_santiago),
        ComunaMascota(nombre="El Bosque", provincia=provincia_santiago),
        ComunaMascota(nombre="San Ramón", provincia=provincia_santiago),
        ComunaMascota(nombre="La Granja", provincia=provincia_santiago),
        ComunaMascota(nombre="La Florida", provincia=provincia_santiago),
        ComunaMascota(nombre="Peñalolén", provincia=provincia_santiago),
        ComunaMascota(nombre="Macul", provincia=provincia_santiago)
    ])

    provincia_chacabuco = ProvinciaMascota.objects.create(nombre="Provincia de Chacabuco", region=region_metropolitana)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Colina", provincia=provincia_chacabuco),
        ComunaMascota(nombre="Lampa", provincia=provincia_chacabuco),
        ComunaMascota(nombre="Tiltil", provincia=provincia_chacabuco)
    ])

    provincia_cordillera = ProvinciaMascota.objects.create(nombre="Provincia de Cordillera", region=region_metropolitana)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Puente Alto", provincia=provincia_cordillera),
        ComunaMascota(nombre="Pirque", provincia=provincia_cordillera),
        ComunaMascota(nombre="San José de Maipo", provincia=provincia_cordillera)
    ])

    provincia_maipo = ProvinciaMascota.objects.create(nombre="Provincia de Maipo", region=region_metropolitana)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="San Bernardo", provincia=provincia_maipo),
        ComunaMascota(nombre="Buin", provincia=provincia_maipo),
        ComunaMascota(nombre="Paine", provincia=provincia_maipo),
        ComunaMascota(nombre="Calera de Tango", provincia=provincia_maipo)
    ])

    provincia_melipilla = ProvinciaMascota.objects.create(nombre="Provincia de Melipilla", region=region_metropolitana)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Melipilla", provincia=provincia_melipilla),
        ComunaMascota(nombre="Alhúe", provincia=provincia_melipilla),
        ComunaMascota(nombre="Curacaví", provincia=provincia_melipilla),
        ComunaMascota(nombre="María Pinto", provincia=provincia_melipilla),
        ComunaMascota(nombre="San Pedro", provincia=provincia_melipilla),
    ])

    provincia_talagante = ProvinciaMascota.objects.create(nombre="Provincia de Talagante", region=region_metropolitana)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Talagante", provincia=provincia_talagante),
        ComunaMascota(nombre="Peñaflor", provincia=provincia_talagante),
        ComunaMascota(nombre="Isla de Maipo", provincia=provincia_talagante),
        ComunaMascota(nombre="El Monte", provincia=provincia_talagante),
        ComunaMascota(nombre="Padre Hurtado", provincia=provincia_talagante)
    ])

    # Región del Libertador General Bernardo O'Higgins (VI)
    libertador_general_bernardo_ohiggins = RegionMascota.objects.create(nombre="Región del Libertador General Bernardo O'Higgins (VI)", pais=chile)

    provincia_cachapoal = ProvinciaMascota.objects.create(nombre="Provincia de Cachapoal", region=libertador_general_bernardo_ohiggins)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Rancagua", provincia=provincia_cachapoal),
        ComunaMascota(nombre="Machalí", provincia=provincia_cachapoal),
        ComunaMascota(nombre="Graneros", provincia=provincia_cachapoal),
        ComunaMascota(nombre="Codegua", provincia=provincia_cachapoal),
        ComunaMascota(nombre="Requínoa", provincia=provincia_cachapoal),
        ComunaMascota(nombre="Rengo", provincia=provincia_cachapoal),
        ComunaMascota(nombre="Olivar", provincia=provincia_cachapoal),
        ComunaMascota(nombre="Doñihue", provincia=provincia_cachapoal),
        ComunaMascota(nombre="Coltauco", provincia=provincia_cachapoal),
        ComunaMascota(nombre="Coinco", provincia=provincia_cachapoal),
        ComunaMascota(nombre="Quinta de Tilcoco", provincia=provincia_cachapoal),
        ComunaMascota(nombre="San Vicente de Tagua Tagua", provincia=provincia_cachapoal),
        ComunaMascota(nombre="Malloa", provincia=provincia_cachapoal),
        ComunaMascota(nombre="Pichidegua", provincia=provincia_cachapoal)
    ])

    provincia_colchagua= ProvinciaMascota.objects.create(nombre="Provincia de Colchagua", region=libertador_general_bernardo_ohiggins)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="San Fernando", provincia=provincia_colchagua),
        ComunaMascota(nombre="Santa Cruz", provincia=provincia_colchagua),
        ComunaMascota(nombre="Chimbarongo", provincia=provincia_colchagua),
        ComunaMascota(nombre="Nancagua", provincia=provincia_colchagua),
        ComunaMascota(nombre="Palmilla", provincia=provincia_colchagua),
        ComunaMascota(nombre="Peralillo", provincia=provincia_colchagua),
        ComunaMascota(nombre="Placilla", provincia=provincia_colchagua),
        ComunaMascota(nombre="Pumanque", provincia=provincia_colchagua),
        ComunaMascota(nombre="Lolol", provincia=provincia_colchagua),
        ComunaMascota(nombre="Chépica", provincia=provincia_colchagua),
    ])

    provincia_cardenal_caro = ProvinciaMascota.objects.create(nombre="Provincia de Cardenal Caro", region=libertador_general_bernardo_ohiggins)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Pichilemu", provincia=provincia_cardenal_caro),
        ComunaMascota(nombre="Marchigüe", provincia=provincia_cardenal_caro),
        ComunaMascota(nombre="Litueche", provincia=provincia_cardenal_caro),
        ComunaMascota(nombre="La Estrella", provincia=provincia_cardenal_caro),
        ComunaMascota(nombre="Paredones", provincia=provincia_cardenal_caro),
        ComunaMascota(nombre="Navidad", provincia=provincia_cardenal_caro)
    ])
    

    # Región del Maule (VII)
    maule = RegionMascota.objects.create(nombre="Región del Maule (VII)", pais=chile)

    provincia_talca = ProvinciaMascota.objects.create(nombre="Provincia de Talca", region=maule)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Talca", provincia=provincia_talca),
        ComunaMascota(nombre="San Clemente", provincia=provincia_talca),
        ComunaMascota(nombre="Pelarco", provincia=provincia_talca),
        ComunaMascota(nombre="Pencahue", provincia=provincia_talca),
        ComunaMascota(nombre="Maule", provincia=provincia_talca),
        ComunaMascota(nombre="Curepto", provincia=provincia_talca),
        ComunaMascota(nombre="Constitución", provincia=provincia_talca),
        ComunaMascota(nombre="Empedrado", provincia=provincia_talca),
        ComunaMascota(nombre="Río Claro", provincia=provincia_talca)
    ])

    provincia_curico = ProvinciaMascota.objects.create(nombre="Provincia de Curicó", region=maule)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Curicó", provincia=provincia_curico),
        ComunaMascota(nombre="Hualañé", provincia=provincia_curico),
        ComunaMascota(nombre="Licantén", provincia=provincia_curico),
        ComunaMascota(nombre="Molina", provincia=provincia_curico),
        ComunaMascota(nombre="Rauco", provincia=provincia_curico),
        ComunaMascota(nombre="Romeral", provincia=provincia_curico),
        ComunaMascota(nombre="Sagrada Familia", provincia=provincia_curico),
        ComunaMascota(nombre="Vichuquén", provincia=provincia_curico)
    ])

    provincia_linares = ProvinciaMascota.objects.create(nombre="Provincia de Linares", region=maule)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Linares", provincia=provincia_linares),
        ComunaMascota(nombre="Longaví", provincia=provincia_linares),
        ComunaMascota(nombre="Colbún", provincia=provincia_linares),
        ComunaMascota(nombre="San Javier", provincia=provincia_linares),
        ComunaMascota(nombre="Villa Alegre", provincia=provincia_linares),
        ComunaMascota(nombre="Yerbas Buenas", provincia=provincia_linares),
        ComunaMascota(nombre="Parral", provincia=provincia_linares)
    ])

    provincia_cauquenes = ProvinciaMascota.objects.create(nombre="Provincia de Cauquenes", region=maule)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Cauquenes", provincia=provincia_cauquenes),
        ComunaMascota(nombre="Chanco", provincia=provincia_cauquenes),
        ComunaMascota(nombre="Pelluhue", provincia=provincia_cauquenes)
    ])

    # Región de Ñuble (XVI)
    ñuble = RegionMascota.objects.create(nombre="Región de Ñuble (XVI)", pais=chile)

    provincia_diguillin = ProvinciaMascota.objects.create(nombre="Provincia de Diguillín", region=ñuble)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Chillán", provincia=provincia_diguillin),
        ComunaMascota(nombre="Chillán Viejo", provincia=provincia_diguillin),
        ComunaMascota(nombre="El Carmen", provincia=provincia_diguillin),
        ComunaMascota(nombre="Pemuco", provincia=provincia_diguillin),
        ComunaMascota(nombre="Pinto", provincia=provincia_diguillin),
        ComunaMascota(nombre="San Ignacio", provincia=provincia_diguillin),
        ComunaMascota(nombre="Yungay", provincia=provincia_diguillin),
        ComunaMascota(nombre="Bulnes", provincia=provincia_diguillin),
        ComunaMascota(nombre="Quillón", provincia=provincia_diguillin)
    ])

    provincia_itata = ProvinciaMascota.objects.create(nombre="Provincia de Itata", region=ñuble)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Cobquecura", provincia=provincia_itata),
        ComunaMascota(nombre="Coelemu", provincia=provincia_itata),
        ComunaMascota(nombre="Ninhue", provincia=provincia_itata),
        ComunaMascota(nombre="Portezuelo", provincia=provincia_itata),
        ComunaMascota(nombre="Quirihue", provincia=provincia_itata),
        ComunaMascota(nombre="Ránquil", provincia=provincia_itata),
        ComunaMascota(nombre="Trehuaco", provincia=provincia_itata)
    ])

    provincia_punilla = ProvinciaMascota.objects.create(nombre="Provincia de Punilla", region=ñuble)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="San Carlos", provincia=provincia_punilla),
        ComunaMascota(nombre="Coihueco", provincia=provincia_punilla),
        ComunaMascota(nombre="Ñiquén", provincia=provincia_punilla),
        ComunaMascota(nombre="San Fabián", provincia=provincia_punilla)
    ])

    # Región del Biobío (VIII))
    biobio = RegionMascota.objects.create(nombre="Región del Biobío (VIII)", pais=chile)

    provincia_concepcion = ProvinciaMascota.objects.create(nombre="Provincia de Concepción", region=biobio)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Concepción", provincia=provincia_concepcion),
        ComunaMascota(nombre="Talcahuano", provincia=provincia_concepcion),
        ComunaMascota(nombre="Hualpén", provincia=provincia_concepcion),
        ComunaMascota(nombre="San Pedro de la Paz", provincia=provincia_concepcion),
        ComunaMascota(nombre="Chiguayante", provincia=provincia_concepcion),
        ComunaMascota(nombre="Penco", provincia=provincia_concepcion),
        ComunaMascota(nombre="Tomé", provincia=provincia_concepcion),
        ComunaMascota(nombre="Coronel", provincia=provincia_concepcion),
        ComunaMascota(nombre="Lota", provincia=provincia_concepcion),
        ComunaMascota(nombre="Hualqui", provincia=provincia_concepcion),
        ComunaMascota(nombre="Santa Juana", provincia=provincia_concepcion),
        ComunaMascota(nombre="Florida", provincia=provincia_concepcion)
    ])

    provincia_arauco = ProvinciaMascota.objects.create(nombre="Provincia de Arauco", region=biobio)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Arauco", provincia=provincia_arauco),
        ComunaMascota(nombre="Coranilahue", provincia=provincia_arauco),
        ComunaMascota(nombre="Lebu", provincia=provincia_arauco),
        ComunaMascota(nombre="Los Álamos", provincia=provincia_arauco),
        ComunaMascota(nombre="Cañete", provincia=provincia_arauco),
        ComunaMascota(nombre="Contulmo", provincia=provincia_arauco),
        ComunaMascota(nombre="Tirúa", provincia=provincia_arauco)
    ])

    provincia_biobio = ProvinciaMascota.objects.create(nombre="Provincia de Biobío", region=biobio)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Los Ángeles", provincia=provincia_biobio),
        ComunaMascota(nombre="Laja", provincia=provincia_biobio),
        ComunaMascota(nombre="Mulchén", provincia=provincia_biobio),
        ComunaMascota(nombre="Nacimiento", provincia=provincia_biobio),
        ComunaMascota(nombre="Negrete", provincia=provincia_biobio),
        ComunaMascota(nombre="San Rosendo", provincia=provincia_biobio),
        ComunaMascota(nombre="Santa Bárbara", provincia=provincia_biobio),
        ComunaMascota(nombre="Quilaco", provincia=provincia_biobio),
        ComunaMascota(nombre="Quileco", provincia=provincia_biobio),
        ComunaMascota(nombre="Yumbel", provincia=provincia_biobio),
        ComunaMascota(nombre="Cabrero", provincia=provincia_biobio),
        ComunaMascota(nombre="Tucapel", provincia=provincia_biobio),
        ComunaMascota(nombre="Alto Biobío", provincia=provincia_biobio)
    ])

    # Región de La Araucanía (IX)
    araucania = RegionMascota.objects.create(nombre="Región de La Araucanía (IX)", pais=chile)

    provincia_cautin = ProvinciaMascota.objects.create(nombre="Provincia de Cautín", region=araucania)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Temuco", provincia=provincia_cautin),
        ComunaMascota(nombre="Padre Las Casas", provincia=provincia_cautin),
        ComunaMascota(nombre="Vilcún", provincia=provincia_cautin),
        ComunaMascota(nombre="Lautaro", provincia=provincia_cautin),
        ComunaMascota(nombre="Perquenco", provincia=provincia_cautin),
        ComunaMascota(nombre="Galvarino", provincia=provincia_cautin),
        ComunaMascota(nombre="Nueva Imperial", provincia=provincia_cautin),
        ComunaMascota(nombre="Cholchol", provincia=provincia_cautin),
        ComunaMascota(nombre="Saavedra", provincia=provincia_cautin),
        ComunaMascota(nombre="Freire", provincia=provincia_cautin),
        ComunaMascota(nombre="Pitrufquén", provincia=provincia_cautin),
        ComunaMascota(nombre="Teodoro Schmidt", provincia=provincia_cautin),
        ComunaMascota(nombre="Toltén", provincia=provincia_cautin),
        ComunaMascota(nombre="Loncoche", provincia=provincia_cautin),
        ComunaMascota(nombre="Gorbea", provincia=provincia_cautin),
        ComunaMascota(nombre="Cunco", provincia=provincia_cautin),
        ComunaMascota(nombre="Melipeuco", provincia=provincia_cautin)
    ])

    provincia_malleco = ProvinciaMascota.objects.create(nombre="Provincia de Malleco", region=araucania)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Angol", provincia=provincia_malleco),
        ComunaMascota(nombre="Renaico", provincia=provincia_malleco),
        ComunaMascota(nombre="Collipulli", provincia=provincia_malleco),
        ComunaMascota(nombre="Ercilla", provincia=provincia_malleco),
        ComunaMascota(nombre="Lonquimay", provincia=provincia_malleco),
        ComunaMascota(nombre="Curicautín", provincia=provincia_malleco),
        ComunaMascota(nombre="Victoria", provincia=provincia_malleco),
        ComunaMascota(nombre="Traiguén", provincia=provincia_malleco),
        ComunaMascota(nombre="Lumaco", provincia=provincia_malleco),
        ComunaMascota(nombre="Los Sauces", provincia=provincia_malleco),
        ComunaMascota(nombre="Purén", provincia=provincia_malleco)
    ])

    # Región de Los Ríos (XIV)
    rios = RegionMascota.objects.create(nombre="Región de Los Ríos (XIV)", pais=chile)

    provincia_valdivia = ProvinciaMascota.objects.create(nombre="Provincia de Valdivia", region=rios)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Valdivia", provincia=provincia_valdivia),
        ComunaMascota(nombre="Corral", provincia=provincia_valdivia),
        ComunaMascota(nombre="Lanco", provincia=provincia_valdivia),
        ComunaMascota(nombre="Máfil", provincia=provincia_valdivia),
        ComunaMascota(nombre="Mariquina", provincia=provincia_valdivia),
        ComunaMascota(nombre="Panguipulli", provincia=provincia_valdivia),
        ComunaMascota(nombre="Los Lagos", provincia=provincia_valdivia),
        ComunaMascota(nombre="Paillaco", provincia=provincia_valdivia)
    ])

    provincia_ranco = ProvinciaMascota.objects.create(nombre="Provincia del Ranco", region=rios)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="La Unión", provincia=provincia_ranco),
        ComunaMascota(nombre="Futrono", provincia=provincia_ranco),
        ComunaMascota(nombre="Lago Ranco", provincia=provincia_ranco),
        ComunaMascota(nombre="Río Bueno", provincia=provincia_ranco)
    ])

    # Región de Los Lagos (X)
    lagos = RegionMascota.objects.create(nombre="Región de Los Lagos (X)", pais=chile)

    provincia_llanquihue = ProvinciaMascota.objects.create(nombre="Provincia de Llanquihue", region=lagos)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Puerto Montt", provincia=provincia_llanquihue),
        ComunaMascota(nombre="Puerto Varas", provincia=provincia_llanquihue),
        ComunaMascota(nombre="Llanquihue", provincia=provincia_llanquihue),
        ComunaMascota(nombre="Frutillar", provincia=provincia_llanquihue),
        ComunaMascota(nombre="Los Muermos", provincia=provincia_llanquihue),
        ComunaMascota(nombre="Fresia", provincia=provincia_llanquihue),
        ComunaMascota(nombre="Maullín", provincia=provincia_llanquihue),
        ComunaMascota(nombre="Calbuco", provincia=provincia_llanquihue)
    ])

    provincia_chiloe = ProvinciaMascota.objects.create(nombre="Provincia de Chiloé", region=lagos)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Castro", provincia=provincia_chiloe),
        ComunaMascota(nombre="Ancud", provincia=provincia_chiloe),
        ComunaMascota(nombre="Chonchi", provincia=provincia_chiloe),
        ComunaMascota(nombre="Dalcahue", provincia=provincia_chiloe),
        ComunaMascota(nombre="Curaco de Vélez", provincia=provincia_chiloe),
        ComunaMascota(nombre="Queilén", provincia=provincia_chiloe),
        ComunaMascota(nombre="Quellón", provincia=provincia_chiloe),
        ComunaMascota(nombre="Quemchi", provincia=provincia_chiloe),
        ComunaMascota(nombre="Puqueldón", provincia=provincia_chiloe)
    ])

    provincia_osorno = ProvinciaMascota.objects.create(nombre="Provincia de Osorno", region=lagos)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Osorno", provincia=provincia_osorno),
        ComunaMascota(nombre="San Pablo", provincia=provincia_osorno),
        ComunaMascota(nombre="San Juan de la Costa", provincia=provincia_osorno),
        ComunaMascota(nombre="Purranque", provincia=provincia_osorno),
        ComunaMascota(nombre="Río Negro", provincia=provincia_osorno),
        ComunaMascota(nombre="Puerto Octay", provincia=provincia_osorno)
    ])

    provincia_palena = ProvinciaMascota.objects.create(nombre="Provincia de Palena", region=lagos)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Chaitén", provincia=provincia_palena),
        ComunaMascota(nombre="Futaleufú", provincia=provincia_palena),
        ComunaMascota(nombre="Palena", provincia=provincia_palena),
        ComunaMascota(nombre="Hualaihúe", provincia=provincia_palena)
    ])

    # Región de Aysén del General Carlos Ibáñez del Campo (XI)
    aysen = RegionMascota.objects.create(nombre="Región de Aysén del General Carlos Ibáñez del Campo (XI)", pais=chile)

    provincia_coyhaique = ProvinciaMascota.objects.create(nombre="Provincia de Coyhaique", region=aysen)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Coyhaique", provincia=provincia_coyhaique),
        ComunaMascota(nombre="Lago Verde", provincia=provincia_coyhaique)
    ])

    provincia_aysen = ProvinciaMascota.objects.create(nombre="Provincia de Aysén", region=aysen)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Aysén", provincia=provincia_aysen),
        ComunaMascota(nombre="Cisnes", provincia=provincia_aysen),
        ComunaMascota(nombre="Guaitecas", provincia=provincia_aysen)
    ])

    provincia_general_carrera = ProvinciaMascota.objects.create(nombre="Provincia de General Carrera", region=aysen)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Chile Chico", provincia=provincia_general_carrera),
        ComunaMascota(nombre="Río Ibáñez", provincia=provincia_general_carrera)
    ])

    provincia_capitan_prat = ProvinciaMascota.objects.create(nombre="Provincia de Capitán Prat", region=aysen)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Cochrane", provincia=provincia_capitan_prat),
        ComunaMascota(nombre="Tortel", provincia=provincia_capitan_prat),
        ComunaMascota(nombre="O'Higgiins", provincia=provincia_capitan_prat)
    ])

    # Región de Magallanes y de la Antártica Chilena (XII)
    magallanes_antartica_chilena = RegionMascota.objects.create(nombre="Región de Magallanes y de la Antártica Chilena (XII)", pais=chile)

    provincia_magallanes = ProvinciaMascota.objects.create(nombre="Provincia de Magallanes", region=magallanes_antartica_chilena)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Punta Arenas", provincia=provincia_magallanes),
        ComunaMascota(nombre="Laguna Blanca", provincia=provincia_magallanes),
        ComunaMascota(nombre="Rio Verde", provincia=provincia_magallanes),
        ComunaMascota(nombre="San Gregorio", provincia=provincia_magallanes)
    ])

    provincia_tierra_fuego = ProvinciaMascota.objects.create(nombre="Provincia de Tierra del Fuego", region=magallanes_antartica_chilena)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Porvenir", provincia=provincia_tierra_fuego),
        ComunaMascota(nombre="Primavera", provincia=provincia_tierra_fuego),
        ComunaMascota(nombre="Timaukel", provincia=provincia_tierra_fuego)
    ])

    provincia_utlima_esperanza = ProvinciaMascota.objects.create(nombre="Provincia de Última Esperanza", region=magallanes_antartica_chilena)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Puerto Natales", provincia=provincia_utlima_esperanza),
        ComunaMascota(nombre="Torres del Paine", provincia=provincia_utlima_esperanza)
    ])

    provincia_antartica_chilena = ProvinciaMascota.objects.create(nombre="Provincia de la Antártica Chilena", region=magallanes_antartica_chilena)
    ComunaMascota.objects.bulk_create([
        ComunaMascota(nombre="Cabo de Hornos", provincia=provincia_antartica_chilena),
        ComunaMascota(nombre="Antártica", provincia=provincia_antartica_chilena)
    ])


    print("Datos cargados exitosamente")

if __name__ == '__main__':
    cargar_datos_mascota()
