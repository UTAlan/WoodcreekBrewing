# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Red Hat, Inc.
# Copyright 2012-2013 Hewlett-Packard Development Company, L.P.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from pbr.tests import base
from pbr import version


class DeferredVersionTestCase(base.BaseTestCase):

    def test_cached_version(self):
        class MyVersionInfo(version.VersionInfo):
            def _get_version_from_pkg_resources(self):
                return "5.5.5.5"

        deferred_string = MyVersionInfo("openstack").\
            cached_version_string()
        self.assertEqual("5.5.5.5", deferred_string)
