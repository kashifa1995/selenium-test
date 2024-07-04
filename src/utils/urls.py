from src.utils.config_manager import conf
import os

# Home page URLs
CTT_HOME_PAGE = list(conf.commercial_truck.ctt_home_page.__dict__.values())
RV_HOME_PAGE = list(conf.rv.rv_home_page.__dict__.values())
CYCLE_HOME_PAGE = list(conf.cycle.cycle_home_page.__dict__.values())
EQUIPMENT_HOME_PAGE = list(conf.equipment.equipment_home_page.__dict__.values())
ATV_HOME_PAGE = list(conf.atv.atv_home_page.__dict__.values())
PWC_HOME_PAGE = list(conf.pwc.pwc_home_page.__dict__.values())
SNOWMOBILE_HOME_PAGE = list(conf.snowmobile.snowmobile_home_page.__dict__.values())
AERO_HOME_PAGE = list(conf.aero.aero_home_page.__dict__.values())
BOAT_HOME_PAGE = list(conf.boat.boat_home_page.__dict__.values())

# Advance search page URLs
CTT_ADVANCE_SEARCH_PAGE = list(conf.commercial_truck.ctt_advance_search_page.__dict__.values())
RV_ADVANCE_SEARCH_PAGE = list(conf.rv.rv_advance_search_page.__dict__.values())
CYCLE_ADVANCE_SEARCH_PAGE = list(conf.cycle.cycle_advance_search_page.__dict__.values())
EQUIPMENT_ADVANCE_SEARCH_PAGE = list(conf.equipment.equipment_advance_search_page.__dict__.values())
ATV_ADVANCE_SEARCH_PAGE = list(conf.atv.atv_advance_search_page.__dict__.values())
PWC_ADVANCE_SEARCH_PAGE = list(conf.pwc.pwc_advance_search_page.__dict__.values())
SNOWMOBILE_ADVANCE_SEARCH_PAGE = list(conf.snowmobile.snowmobile_advance_search_page.__dict__.values())
AERO_ADVANCE_SEARCH_PAGE = list(conf.aero.aero_advance_search_page.__dict__.values())
BOAT_ADVANCE_SEARCH_PAGE = list(conf.boat.boat_advance_search_page.__dict__.values())

# Search Result page URLs
CTT_SEARCH_PAGE = list(conf.commercial_truck.ctt_search_page.__dict__.values())
RV_SEARCH_PAGE = list(conf.rv.rv_search_page.__dict__.values())
CYCLE_SEARCH_PAGE = list(conf.cycle.cycle_search_page.__dict__.values())
EQUIPMENT_SEARCH_PAGE = list(conf.equipment.equipment_search_page.__dict__.values())
ATV_SEARCH_PAGE = list(conf.atv.atv_search_page.__dict__.values())
PWC_SEARCH_PAGE = list(conf.pwc.pwc_search_page.__dict__.values())
SNOWMOBILE_SEARCH_PAGE = list(conf.snowmobile.snowmobile_search_page.__dict__.values())
AERO_SEARCH_PAGE = list(conf.aero.aero_search_page.__dict__.values())
BOAT_SEARCH_PAGE = list(conf.boat.boat_search_page.__dict__.values())

# Dealer page URLs
CTT_DEALER_PAGE = list(conf.commercial_truck.ctt_dealer_page.__dict__.values())
RV_DEALER_PAGE = list(conf.rv.rv_dealer_page.__dict__.values())
CYCLE_DEALER_PAGE = list(conf.cycle.cycle_dealer_page.__dict__.values())
EQUIPMENT_DEALER_PAGE = list(conf.equipment.equipment_dealer_page.__dict__.values())
ATV_DEALER_PAGE = list(conf.atv.atv_dealer_page.__dict__.values())
PWC_DEALER_PAGE = list(conf.pwc.pwc_dealer_page.__dict__.values())
SNOWMOBILE_DEALER_PAGE = list(conf.snowmobile.snowmobile_dealer_page.__dict__.values())
AERO_DEALER_PAGE = list(conf.aero.aero_dealer_page.__dict__.values())
BOAT_DEALER_PAGE = list(conf.boat.boat_dealer_page.__dict__.values())

# Dealer Group Page URLs
CTT_DEALER_GROUP_PAGE = list(conf.commercial_truck.ctt_dealer_group_page.__dict__.values())
CTT_DEALER_GROUP_PAGE_FOR_TRAILERS = list(
    conf.commercial_truck.ctt_dealer_group_page_for_trailer_filter.__dict__.values())
RV_DEALER_GROUP_PAGE = list(conf.rv.rv_dealer_group_page.__dict__.values())
CYCLE_DEALER_GROUP_PAGE = list(conf.cycle.cycle_dealer_group_page.__dict__.values())
EQUIPMENT_DEALER_GROUP_PAGE = list(conf.equipment.equipment_dealer_group_page.__dict__.values())
ATV_DEALER_GROUP_PAGE = list(conf.atv.atv_dealer_group_page.__dict__.values())
PWC_DEALER_GROUP_PAGE = list(conf.pwc.pwc_dealer_group_page.__dict__.values())
SNOWMOBILE_DEALER_GROUP_PAGE = list(conf.snowmobile.snowmobile_dealer_group_page.__dict__.values())
BOAT_DEALER_GROUP_PAGE = list(conf.boat.boat_dealer_group_page.__dict__.values())

# Dealer Gallery Page URLs
CTT_DEALER_GALLERY_PAGE = list(conf.commercial_truck.ctt_dealer_gallery_page.__dict__.values())
CTT_DEALER_GALLERY_PAGE_FOR_TRAILERS = list(
    conf.commercial_truck.ctt_dealer_gallery_page_for_trailer_filter.__dict__.values())
RV_DEALER_GALLERY_PAGE = list(conf.rv.rv_dealer_gallery_page.__dict__.values())
CYCLE_DEALER_GALLERY_PAGE = list(conf.cycle.cycle_dealer_gallery_page.__dict__.values())
EQUIPMENT_DEALER_GALLERY_PAGE = list(conf.equipment.equipment_dealer_gallery_page.__dict__.values())
ATV_DEALER_GALLERY_PAGE = list(conf.atv.atv_dealer_gallery_page.__dict__.values())
PWC_DEALER_GALLERY_PAGE = list(conf.pwc.pwc_dealer_gallery_page.__dict__.values())
SNOWMOBILE_DEALER_GALLERY_PAGE = list(conf.snowmobile.snowmobile_dealer_gallery_page.__dict__.values())
AERO_DEALER_GALLERY_PAGE = list(conf.aero.aero_dealer_gallery_page.__dict__.values())
BOAT_DEALER_GALLERY_PAGE = list(conf.boat.boat_dealer_gallery_page.__dict__.values())

#Buy Online Page
CYCLE_BUY_ONLINE_PAGE = list(conf.cycle.cycle_buy_online_page.__dict__.values())

# # Vehicle Detailing Page URLS
if "ENV" in os.environ and "dev" not in os.environ["ENV"]:
    CTT_VDP = list(conf.commercial_truck.ctt_vdp_prod.__dict__.values())
    RV_VDP = list(conf.rv.rv_vdp_prod.__dict__.values())
    CYCLE_VDP = list(conf.cycle.cycle_vdp_prod.__dict__.values())
    EQUIPMENT_VDP = list(conf.equipment.equipment_vdp_prod.__dict__.values())
    ATV_VDP = list(conf.atv.atv_vdp_prod.__dict__.values())
    PWC_VDP = list(conf.pwc.pwc_vdp_prod.__dict__.values())
    SNOWMOBILE_VDP = list(conf.snowmobile.snowmobile_vdp_prod.__dict__.values())
    AERO_VDP = list(conf.aero.aero_vdp_prod.__dict__.values())
    BOAT_VDP = list(conf.boat.boat_vdp_prod.__dict__.values())
else:
    CTT_VDP = list(conf.commercial_truck.ctt_vdp_dev.__dict__.values())
    RV_VDP = list(conf.rv.rv_vdp_dev.__dict__.values())
    CYCLE_VDP = list(conf.cycle.cycle_vdp_dev.__dict__.values())
    EQUIPMENT_VDP = list(conf.equipment.equipment_vdp_dev.__dict__.values())
    ATV_VDP = list(conf.atv.atv_vdp_dev.__dict__.values())
    PWC_VDP = list(conf.pwc.pwc_vdp_dev.__dict__.values())
    SNOWMOBILE_VDP = list(conf.snowmobile.snowmobile_vdp_dev.__dict__.values())
    AERO_VDP = list(conf.aero.aero_vdp_dev.__dict__.values())
    BOAT_VDP = list(conf.boat.boat_vdp_dev.__dict__.values())

# keyword Input
ctt_keyword_input = conf.commercial_truck.keyword_input
rv_keyword_input = conf.rv.keyword_input
cycle_keyword_input = conf.cycle.keyword_input
equipment_keyword_input = conf.equipment.keyword_input
atv_keyword_input = conf.atv.keyword_input
pwc_keyword_input = conf.pwc.keyword_input
snowmobile_keyword_input = conf.snowmobile.keyword_input
aero_keyword_input = conf.aero.keyword_input
boat_keyword_input = conf.boat.keyword_input

# Make Input
ctt_make_input = conf.commercial_truck.make_input
rv_make_input = conf.rv.make_input
cycle_make_input = conf.cycle.make_input
equipment_make_input = conf.equipment.make_input
atv_make_input = conf.atv.make_input
pwc_make_input = conf.pwc.make_input
snowmobile_make_input = conf.snowmobile.make_input
aero_make_input = conf.aero.make_input
boat_make_input = conf.boat.make_input

# Model Input
ctt_model_input = conf.commercial_truck.model_input
rv_model_input = conf.rv.model_input
cycle_model_input = conf.cycle.model_input
atv_model_input = conf.atv.model_input
pwc_model_input = conf.pwc.model_input
snowmobile_model_input = conf.snowmobile.model_input
aero_model_input = conf.aero.model_input
boat_model_input = conf.boat.model_input

# Dealer name Input
ctt_dealer_name_input = conf.commercial_truck.dealer_name_input
rv_dealer_name_input = conf.rv.dealer_name_input
cycle_dealer_name_input = conf.cycle.dealer_name_input
equipment_dealer_name_input = conf.equipment.dealer_name_input
atv_dealer_name_input = conf.atv.dealer_name_input
pwc_dealer_name_input = conf.pwc.dealer_name_input
snowmobile_dealer_name_input = conf.snowmobile.dealer_name_input
aero_dealer_name_input = conf.aero.dealer_name_input
boat_dealer_name_input = conf.boat.dealer_name_input
