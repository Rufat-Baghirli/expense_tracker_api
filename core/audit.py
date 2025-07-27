import logging

audit_logger = logging.getLogger("audit")

def log_user_action(user, action, extra=None):
    audit_logger.info(f"User: {user.id if user else 'Anonymous'} | Action: {action} | Extra: {extra}")