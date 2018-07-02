import xml.etree.ElementTree as ET

tree1 = ET.parse('xml1.xml')
tree2 = ET.parse('xml2.xml')

e1 = ET.ElementTree(tree1)
e2 = ET.ElementTree(tree2)

for elt1 in e1.iter('project'):
        for elt2 in e2.iter('project'):
            if(elt1.text == elt2.text and elt2.find('path').text != elt1.find('path').text) :
                # if(elt1.find('path') == elt2.find('path')):
                    path_list = elt2.find('path').text
                    print path_list

# for child in tree1.iter('project'):
#    print child.tag, child.attrib, child.text

