---
box_periodicity:
  headers: ['ppp', 'ppf']
  links:
  - assets/img/DC_Cu110/DC_Cu110_ppp.gif
  - assets/img/DC_Cu110/DC_Cu110_ppf.gif
temperature:
  headers: ['150 K', '175 K', '200 K', '225 K', '250 K']
  links:
  - assets/img/DC_Cu110/DC_Cu110_ppp_T150.gif
  - assets/img/DC_Cu110/DC_Cu110_ppp_T175.gif
  - assets/img/DC_Cu110/DC_Cu110_ppp_T200.gif
  - assets/img/DC_Cu110/DC_Cu110_ppp_T225.gif
  - assets/img/DC_Cu110/DC_Cu110_ppp_T250.gif
box_size:
  headers: ['2 nm', '3 nm', '4 nm', '5 nm']
  links:
  - assets/img/DC_Cu110/DC_Cu110_ppp_z20.gif
  - assets/img/DC_Cu110/DC_Cu110_ppp_z30.gif
  - assets/img/DC_Cu110/DC_Cu110_ppp_z40.gif
  - assets/img/DC_Cu110/DC_Cu110_ppp_z50.gif
---
### Tests
-   Periodic vs non-periodic *z-direction*
-   Temperature
-   Box size
-   Decacylene - slab distance

## Box Periodicity

<table><tr>{% for head in page.box_periodicity.headers %}<th>{{ head }}</th>{% endfor %}</tr>
<tr>{% for link in page.box_periodicity.links %}<th><a href="{{ link }}">
<img src="{{ link }}"></a></th>{% endfor %}</tr></table>

### Temperature

<table>
  <tr>{% for head in page.temperature.headers %}<th>{{ head }}</th>{% endfor %}</tr>
  <tr>
    {% for link in page.temperature.links %}
      <th><a href="{{ link }}"><img src="{{ link }}"></a></th>
    {% endfor %}
  </tr>
</table>

### Box size

#### *z-direction*

<table>
  <tr>{% for head in page.box_size.headers %}<th>{{ head }}</th>{% endfor %}</tr>
  <tr>
    {% for link in page.box_size.links %}
      <th><a href="{{ link }}"><img src="{{ link }}"></a></th>
    {% endfor %}
  </tr>
</table>

#### *xy-plane*

<table>
  <tr>{% for head in page.box_size.headers %}<th>{{ head }}</th>{% endfor %}</tr>
  <tr>
    {% for link in page.box_size.links %}
      <th><a href="{{ link }}"><img src="{{ link }}"></a></th>
    {% endfor %}
  </tr>
</table>
