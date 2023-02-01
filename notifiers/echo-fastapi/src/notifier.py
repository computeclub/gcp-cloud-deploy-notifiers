# -*- coding: utf-8 -*-
from typing import Any, Dict
from clouddeploy_notifier.notifier import BaseNotifier
import logging

logger = logging.getLogger(__name__)


class Notifier(BaseNotifier):
    """Notifier implements action for this use-case."""

    def action(self, config: Dict[str, Any], **kwargs) -> None:
        """
        The action here is just for demonstration purposes. It echos back the
        pubsub message and the configuration fetched.
        """
        logging.debug("executing the action")
        logging.info("config: %s", config)
        logging.info("kw_arg_example: %s", kwargs["kw_arg_example"])
        logging.info("message_attributes: %s", kwargs["message_attributes"].json())
        logging.debug("action completed successfully")
