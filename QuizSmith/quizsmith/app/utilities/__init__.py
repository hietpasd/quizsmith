#
#   Copyright 2014 UW Board of Regents
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from quizsmith.app.utilities.security import ACL,RootACL,PyramidFormalchemyACL,groupfinder,RequestExtension
from quizsmith.app.utilities.utility import Validate,Result2Dict,Seconds2Str,RemoveImages,add_route
from quizsmith.app.utilities.test import TestCreator,TestManager
