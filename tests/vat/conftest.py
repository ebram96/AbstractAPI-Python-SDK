import pytest


@pytest.fixture
def vat_validation_sample():
    return {
        "vat_number": "SE556656688001",
        "valid": True,
        "company": {
            "name": "GOOGLE SWEDEN AB",
            "address": "GOOGLE IRLAND LTD \nM COLLINS, GORDON HOUSE \nBARROW STREET, DUBLIN 4 \nIRLAND"
        },
        "country": {
            "code": "SE",
            "name": "Sweden"
        }
    }


@pytest.fixture
def vat_calculation_sample():
    return {
        "amount_excluding_vat": "100.00",
        "amount_including_vat": "119.00",
        "vat_amount": "19.00",
        "vat_category": "standard",
        "vat_rate": "0.190",
        "country": {
            "code": "DE",
            "name": "Germany"
        }
    }


@pytest.fixture
def vat_categories_sample():
    return [
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "water",
            "description": "Supply of water. No reduced rate for bottled water."
        },
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "foodstuffs",
            "description": "Foodstuffs (including beverages but excluding alcoholic beverages) for human and animal consumption; live animals, seeds, plants and ingredients normally intended for use in the preparation of foodstuffs; products normally used to supplement foodstuffs or as a substitute for foodstuffs. Reduced rate only on part of the items."
        },
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "sculpture art",
            "description": "Original sculptures and statuary, in any material, provided that they are executed entirely by the artists."
        },
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "social welfare goods",
            "description": "Supply of goods and services by organisations recognised as being devoted to social wellbeing by Member States and engaged in welfare or social security work."
        },
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "art services",
            "description": "Supply of services by writers, composers and performing artists, or of the royalties due to them."
        },
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "newspapers",
            "description": "Newspapers. Reduced rate not applicable to newspapers whose content is harmful to minors or is predominatly devoted to advertising."
        },
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "description",
            "description": "Pictures, collages and similar decorative plaques, paintings and drawings, executed entirely by hand by the artist, other than plans and drawings for architectural, engineering, industrial, commercial, topographical or similar purposes, hand-decorated manufactured articles, theatrical scenery, studio back cloths or the like of painted canvas (CN code 9701)."
        },
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "medical",
            "description": "Provision of medical and dental care and thermal treatment. Reduced rate on part of the items."
        },
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "engravings prints lithographs",
            "description": "Original engravings, prints and lithographs, being impressions produced in the limited numbers directly in black and white or in colour of one or of several plates executed entirely by hand by the artist, irrespective of the process or of the material employed, but not including any mechanical or photomechanical process (CN code 9702 00 00)."
        },
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "passenger transport",
            "description": "Transport of passengers and their accompanying luggage. Reduced rate on local transport and rail-bound transport in long-distance."
        },
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "accommodation",
            "description": "Accommodation provided in hotels and similar establishments, including the provision of holiday accommodation and the letting of places on camping or caravan sites. Only for short-term accommodation."
        },
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "periodicals",
            "description": "Periodicals. Reduced rate not applicable to periodicals whose content is harmful to minors or is predominatly devoted to advertising."
        },
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "admission to entertainment events",
            "description": "Admission to shows, theatres, circuses, fairs, amusement parks, concerts, museums, zoos, cinemas, exhibitions and similar cultural events and facilities. Reduced rate only on part of the items."
        },
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "sculpture cast art",
            "description": "Sculpture casts the production of which is limited to eight copies and supervised by the artist or his successors in title (CN code 9703 00 00) on an exceptional basis, in cases determined by the Member States, the limit of eight copies may be exceeded for statuary casts produced before 1 January 1989."
        },
        {
            "country_code": "DE",
            "rate": "0.190",
            "category": "collections or collectors pieces",
            "description": "Collections and collector’s pieces of zoological, botanical, mineralogical, ethnographic or numismatic interest (CN code 9705 00 00)."
        },
        {
            "country_code": "DE",
            "rate": "0.190",
            "category": "standard",
            "description": ""
        },
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "books",
            "description": "Supply, including on loan by libraries, of books, newspapers and periodicals either on physical means of support or supplied electronically or both (including brochures, leaflets and similar printed matter, children's picture, drawing or colouring books, music printed or in manuscript form, maps and hydrographic or similar charts), other than publications wholly or predominantly devoted to advertising and other than publications wholly or predominantly consisting of video content or audible music. Reduced rate only on part of the items."
        },
        {
            "country_code": "DE",
            "rate": "0.070",
            "category": "picture art",
            "description": "Pictures, collages and similar decorative plaques, paintings and drawings, executed entirely by hand by the artist, other than plans and drawings for architectural, engineering, industrial, commercial, topographical or similar purposes, hand-decorated manufactured articles, theatrical scenery, studio back cloths or the like of painted canvas (CN code 9701)."
        }
    ]
